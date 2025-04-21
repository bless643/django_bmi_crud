from django.db import models


# Create your models here.
class BMI(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField(default=0)
    bmi_status = models.CharField(max_length=30, default="NOT YET")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name









