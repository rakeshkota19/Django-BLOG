# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#text field more size char field less size
class Articles(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    thumb=models.ImageField(default='default.png',blank=True)
    author=models.ForeignKey(User,default=None)


# defines how article is going to look in admin section and shell(in built function)
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]
