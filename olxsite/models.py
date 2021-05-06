from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics/%y/%m/%d', max_length=255)
    details = models.TextField()


class VideoInfo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    video_length = models.DecimalField(decimal_places=1, max_digits=6)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    tname = models.CharField(max_length=50)
    class_choices = (
        ('btechcse1', 'BTech(CSE) 1st Sem'),
        ('btechcse2', 'BTech(CSE) 2nd Sem'),
        ('btechcse3', 'BTech(CSE) 3rd Sem'),
        ('btechcse4', 'BTech(CSE) 4th Sem'),
        ('btechcse5', 'BTech(CSE) 5th Sem'),
        ('btechcse6', 'BTech(CSE) 6th Sem'),
    )
    teacher_class = models.CharField(max_length=50, choices=class_choices)
    dob = models.DateField()
    married = models.BooleanField()
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choices, max_length=6)

    def __str__(self):
        return self.tname
