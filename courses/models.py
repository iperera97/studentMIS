from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .import validators


COURSE_LEVELS = (
    ("", 'Please select Level'),
    ('certificate', 'Certificate'),
    ('diploma', 'Diploma'),
    ('hnd', 'Higher National Diploma (HND)'),
    ('degree', 'Degree')
)


# Course Model goes here
class Course(models.Model):

    # Properties
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    level = models.CharField(choices=COURSE_LEVELS, max_length=50)
    fee = models.FloatField()
    installment = models.IntegerField()
    register = models.DateField(auto_now_add=True)
    duration = models.IntegerField()  # months

    # Methods
    def __str__(self):
        return "({}) {}".format(self.pk, self.title)

    @property
    def installmentFee(self):
        return self.fee / self.installment

    @property
    def duration_year(self):
        hasYearOrMonth = self.duration % 12
        getAcutalYear = int(self.duration / 12)

        # can get acutal year
        if hasYearOrMonth == 0:

            return "{} {}".format(getAcutalYear, "year") if getAcutalYear == 1 else "{} {}".format(
                getAcutalYear, "years")
        else:

            month = self.duration - (getAcutalYear * 12)
            return "{} months".format(month) if getAcutalYear == 0 else "{} years {} months".format(getAcutalYear, month)

    @property
    def countActiveBatch(self):
        count = Course.objects.filter(
            batch__course_id=self.id, batch__active=True).count()
        return count

    @property
    def totalBatch(self):
        count = Course.objects.filter(batch__course_id=self.id).count()
        return count


# create slug
def create_slug(sender, instance, *args, **kwargs):

    slug = slugify(instance.title)
    instance.slug = slug


pre_save.connect(create_slug, sender=Course)
