from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="blogs"
    )

    title = models.CharField(max_length=250)

    slug = models.SlugField(blank=True, unique=True)

    image = models.ImageField(upload_to="artworks/")

    short_description = models.CharField(max_length=300)

    description = models.TextField()

    artist = models.CharField(max_length=100, default="Rozey")

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args,**kwargs)

    def __str__(self):
        return self.title