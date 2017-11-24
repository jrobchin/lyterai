import os
import csv

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from hub.models import MLModel, Example

class Command(BaseCommand):
    help = 'Seed hub models'

    def handle(self, *args, **options):
        print("Seeding hub...")
        self.hub_seeder()

    def hub_seeder(self):
        print(" Seeding models...")
        with open(os.path.join(os.path.dirname(__file__), "mlmodels.csv"), "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("  Seeding model:", row['name'])
                try:
                    model = MLModel.objects.filter(slug=row['slug']).first()
                    if not model:
                        model = MLModel(
                                name = row['name'],
                                category = row['category'],
                                description=row['description'], 
                                about=row['about'], 
                                slug=row['slug'], 
                                model=row['model'], 
                                weights=row['weights'], 
                                accuracy=row['accuracy']
                            )
                        if row['image']:
                            image_path = os.path.join(settings.MEDIA_ROOT, row['image'])
                            model.image.save(os.path.basename(row['image']), File(open(image_path, "rb")))
                        model.save()
                except IntegrityError as e:
                    print("  {} already exists with an image, truncate db or delete row to re-seed.".format(row['name']))

        print(" Seeding examples...")
        with open(os.path.join(os.path.dirname(__file__), "examples.csv"), "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    model = MLModel.objects.filter(slug=row['model_slug']).first()
                    print(model, row['model_slug'])
                    if model:
                        print("  Seeding example for:", model)
                        example = Example(ml_model=model, description=row['description'], source=row['source'])
                        example.image.save(os.path.basename(row['image']), File(open(os.path.join(settings.BASE_DIR, row['image']), "rb")))
                    else:
                        print("   No model found for example.")
                except IntegrityError as e:
                    print(e)

        print("  Seeded models...")

        return 1