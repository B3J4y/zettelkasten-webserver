from django.db import models


class Category(models.Model):
    """ Categories in which the zettels are sorted """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Zettel(models.Model):
    """ The representation of a Zettel """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date_of_publication = models.DateField('date published')
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)


class Directory(models.Model):
    """ Directory to Zettelkasten with metadata """
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=1000)
    zettel_count = models.IntegerField(default=0)
    category_count = models.IntegerField(default=0)
    last_date_of_zettel = models.DateField('last zettel')
