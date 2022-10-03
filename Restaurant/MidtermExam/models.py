from django.db import models

# Create your models here.


class Employee(models.Model):
    type_user = (('s', 'Waiter'), ('T', 'Manager'))
    EmployeeID = models.CharField(max_length=15, null=False, primary_key=True)
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=1, choices=type_user)


class Table(models.Model):
    tablenbr = models.IntegerField(default=1, null=False, primary_key=True)
    tablenbrseats = models.IntegerField(default=1, null=False)
    tablerating = models.IntegerField(default=1, null=False)


class Manager(Employee):
    monthly = models.FloatField(default=20, null=False)


class Waiter(Employee):
    hourlywage = models.FloatField(default=20, null=False)



class Specialty(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=10)

    class Meta:
        unique_together = ('waiter', 'specialty')


class Seating(models.Model):
    SeatingID = models.CharField(max_length=15, null=False, primary_key=True)
    nbr_of_guest = models.CharField(max_length=18, null=False)
    StartTimeDate = models.DateField(null=False)
    EndTimeDate = models.DateField(null=False)
    table = models.ManyToManyField(Table)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)


class TipsEarned(models.Model):
    tips = models.FloatField(default=2, null=False)
    seating = models.ForeignKey(Seating, on_delete=models.CASCADE)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)




