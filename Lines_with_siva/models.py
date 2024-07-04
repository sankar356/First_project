# from django.db import models
#
#
# # Create your models here.
# class Poet(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class SivaSPoem(models.Model):
#     title = models.CharField(max_length=100)
#     poems = models.ImageField()
#     journel = models.CharField(max_length=100)
#
#
#
# class Books(models.Model):
#     title = models.CharField(SivaSPoem, max_length=200, on_delete=models.CASCADE)
#     author = models.ForeignKey(Poet, on_delete=models.CASCADE)
#     publication_date = models.DateField()
#     bookType = models.CharField(max_length=200)
#     theme = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.title
#
#
#
