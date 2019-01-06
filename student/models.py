from django.db import models
from batch.models import Batch

TITLE_CHOICES = (
    ("", 'Please select your title'),
    ('Mr', 'Mr'),
    ('Miss', 'Miss'),
    ('Mrs', 'Mrs'),
    ('Rev', 'Rev'),
    ('Dr', 'Dr'),
)

GENDER_TYPES = (
    (True, 'Male'),
    (False, 'Female')
)


# Create your models here.
class Student(models.Model):

    title = models.CharField(choices=TITLE_CHOICES,
                             max_length=15, blank=False)
    initals = models.CharField(max_length=25)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.BooleanField(choices=GENDER_TYPES)
    email = models.EmailField(max_length=255)
    register = models.ManyToManyField(Batch, through='Registration')

    def __str__(self):
        return "(#{}) {}".format(self.pk, self.first_name)


class Registration(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    reg_fee = models.FloatField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
