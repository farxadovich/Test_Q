from django.db import models


class Category(models.Model):
    nomi = models.CharField(max_length=45)

    def __str__(self):
        return self.nomi


class Questions(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Choice(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    correct = models.BooleanField()

    def __str__(self):
        return self.text
