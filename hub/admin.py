from django.contrib import admin

from .models import MLModel, Layer, Example

class LayerAdmin(admin.ModelAdmin):
	list_filter = ('name', 'layer_type', 'ml_model', 'input_shape', 'output_shape')
	list_display = ('name', 'layer_type', 'ml_model', 'input_shape', 'output_shape')

class LayerInline(admin.StackedInline):
    model = Layer
    extra = 1
    show_change_link = True

class ExampleInline(admin.StackedInline):
    model = Example
    extra = 1
    show_change_link = True

class MLModelAdmin(admin.ModelAdmin):
	inlines = [LayerInline, ExampleInline]
	date_hierarchy = 'updated_at'
	list_filter = ('name', 'category', 'accuracy', 'updated_at')
	list_display = ('name', 'category', 'accuracy', 'updated_at')


# Register your models here.
admin.site.register(MLModel, MLModelAdmin)
admin.site.register(Layer, LayerAdmin)