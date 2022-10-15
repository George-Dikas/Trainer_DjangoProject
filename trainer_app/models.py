from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        ordering = ["lastname", "firstname", "subject"]

    def __str__(self):
        return self.lastname + ' ' + self.firstname
