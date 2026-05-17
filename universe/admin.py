from django.contrib import admin
from django.utils.html import mark_safe
from .models import ObjectCategory, AstronomicalObject

@admin.register(ObjectCategory)
class ObjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(AstronomicalObject)
class AstronomicalObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'object_type', 'distance_from_earth', 'scale_level', 'image_preview_thumbnail')
    list_filter = ('object_type', 'scale_level')
    search_fields = ('name', 'short_description', 'full_description', 'discovered_by')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_preview_large', 'created_at')
    ordering = ('name', 'object_type')

    fieldsets = (
        ('Basic Information', {
            'fields': (('name', 'slug'), 'object_type', 'image', 'image_preview_large')
        }),
        ('Descriptions', {
            'fields': ('short_description', 'full_description')
        }),
        ('Physical Characteristics', {
            'fields': (('diameter_km', 'mass'), 'distance_from_earth', 'scale_level')
        }),
        ('Discovery & History', {
            'fields': (('discovered_by', 'discovery_date'), 'formation')
        }),
        ('Fun Facts & Context', {
            'fields': ('scientific_fact', 'comparison_to_earth'),
            'classes': ('collapse',)
        }),
        ('System Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def image_preview_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px; border-radius: 4px;" />')
        return "No Image"
    image_preview_thumbnail.short_description = 'Preview'

    def image_preview_large(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 300px; max-width: 300px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />')
        return "No Image Uploaded"
    image_preview_large.short_description = 'Image Preview'
