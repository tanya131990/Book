from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images', blank=True)  # Картинка книги
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_discount_price(self):
        if self.discount_price:
            return self.discount_price
        return self.price
