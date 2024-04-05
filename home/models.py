from django.db import models

# Create your models here.

from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField()

    def __str__(self):
        return self.title

class About(models.Model):
    bio = models.TextField()
    image = models.ImageField(upload_to='about_images/')
    # Assuming you have some fields for social media links
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    # Add more social media fields as needed

    def __str__(self):
        return "About"

class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return "Home"
