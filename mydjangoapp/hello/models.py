from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    hire_date = models.DateField()
    job_id = models.CharField(max_length=10)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return self.first_name+self.last_name