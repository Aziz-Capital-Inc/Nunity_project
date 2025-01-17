from django.db import models

# Create your models here.
class StudentDats(models.Model):
    GENDER_CHOICE = (
        ('male', 'male'),
        ('female', 'female')
    )
    names=models.CharField(max_length=120)
    email=models.EmailField(max_length=200)
    birth_date=models.DateField()
    address=models.CharField(max_length=250)
    gender=models.CharField(max_length=8, choices=GENDER_CHOICE)

    def __str__(self) -> str:
        return self.names


