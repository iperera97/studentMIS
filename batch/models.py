from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.utils.text import slugify
from courses.models import Course


class Batch(models.Model):

    name = models.CharField(max_length=50, verbose_name="batch name")
    slug = models.SlugField(max_length=50)
    register = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    maximum_student_count = models.IntegerField(default=0)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("name", "course"),)

    def __str__(self):
        return "(#{}) {}".format(self.pk, self.name)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)


def createSlug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)


pre_save.connect(createSlug, sender=Batch)
