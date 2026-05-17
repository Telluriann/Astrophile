from django.db import models

class ObjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Object Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class AstronomicalObject(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    object_type = models.ForeignKey(ObjectCategory, on_delete=models.PROTECT, related_name='astronomical_objects')
    short_description = models.TextField(help_text="A brief summary")
    full_description = models.TextField()
    diameter_km = models.FloatField(null=True, blank=True, help_text="Diameter in kilometers")
    mass = models.CharField(max_length=100, null=True, blank=True, help_text="Mass (e.g., '5.97 x 10^24 kg')")
    distance_from_earth = models.CharField(max_length=100, null=True, blank=True, help_text="Distance from Earth (e.g., '4.24 light-years')")
    formation = models.CharField(max_length=200, null=True, blank=True, help_text="Estimated age or formation period")
    discovered_by = models.CharField(max_length=200, null=True, blank=True)
    discovery_date = models.CharField(max_length=100, null=True, blank=True, help_text="Date or era of discovery")
    image = models.ImageField(upload_to='astronomical_objects/', null=True, blank=True)
    scientific_fact = models.TextField(null=True, blank=True)
    comparison_to_earth = models.TextField(null=True, blank=True)
    scale_level = models.IntegerField(default=0, help_text="Used for scale comparisons (e.g., 1=Planet, 2=Star)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
