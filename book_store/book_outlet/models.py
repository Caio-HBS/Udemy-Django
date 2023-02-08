from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Adress Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()


# Creates the model with the desired fields.
class Book(models.Model):
    title = models.CharField(max_length=100)
    # Specifies the field to always be and interger between 1 and 5.
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    # Assigns the foreign key of author to the author variable in this table, 
    # also tells Django to delete the column should something be erased. 
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    # Creates a slug field that is to be used as index for performance.
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)

    # Overrides the get_absolute_url method to point the correct slug.
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    # Overrides the save feature to  include  the slug, also  calls the super to
    # make sure none of the original save features were lost.
    # def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        # super().save(*args, **kwargs)

    # Overrides the way to present the string.
    def __str__(self):
        return f"{self.title} ({self.rating})"
