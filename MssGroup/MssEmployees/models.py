from django.db import models


#
# Create your models here.
class Employees(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=20)
    employee_number = models.IntegerField()
    employee_age = models.IntegerField()

    def __str__(self):
        return self.employee_name


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


# id = models.IntegerField()
# manager = models.CharField(max_length=100)
# hr = models.CharField(max_length=100)
# developer = models.CharField(max_length=100)
# designer =models.CharField(max_length=100)

class Roles(models.Model):
    id_role = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    work_roles = models.CharField(max_length=100)



class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    id_role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    years_of_experience = models.IntegerField(max_length=100)
    employee_num = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name





class User_details(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    id_role = models.ForeignKey(Roles,  on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class UserData(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.user_name
# user
# role
# userdetail ID, UserID,roleID