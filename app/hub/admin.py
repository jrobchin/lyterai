from django.contrib import admin

from .models import MLModel, Layer, Example, Dimension, Preprocessor, DemoResults

class DemoResultsInline(admin.StackedInline):
    model = DemoResults
    extra = 1
    show_change_link = True

class LayerInline(admin.StackedInline):
    model = Layer
    extra = 1
    show_change_link = True

class ExampleInline(admin.StackedInline):
    model = Example
    extra = 1
    show_change_link = True

class DimensionInline(admin.StackedInline):
    model = Dimension
    extra = 1
    show_change_link = True

class PreprocessorInline(admin.StackedInline):
    model = Preprocessor
    extra = 1
    show_change_link = True

class MLModelAdmin(admin.ModelAdmin):
	inlines = [DimensionInline, PreprocessorInline, LayerInline, ExampleInline, DemoResultsInline]
	date_hierarchy = 'updated_at'
	list_filter = ('name', 'category', 'accuracy', 'updated_at')
	list_display = ('name', 'category', 'accuracy', 'updated_at')


# Register your models here.
admin.site.register(MLModel, MLModelAdmin)