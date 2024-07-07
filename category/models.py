import uuid
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.category_name)}-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog'
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
