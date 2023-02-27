from django.db import models
from django.core.validators import(
    MinValueValidator,
    MaxValueValidator
)


class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email_address})"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts_images", null=True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} - Por: {self.author}, ({self.date})"

class Comment(models.Model):
    username = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=254)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment_text = models.TextField(max_length=500)
    parent_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"({self.username} - rating: {self.rating})"
