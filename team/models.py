from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)


class Memeber(models.Model):
    member_name = models.CharField(max_length=255)
    posistion = models.CharField(max_length=120)
    phone_number = models.PositiveBigIntegerField()
    skills = models.ManyToManyField(Skill)
    picture = models.ImageField(upload_to="images/team/")
    email = models.EmailField()
    belongs_to = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_name
