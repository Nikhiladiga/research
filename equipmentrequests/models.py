from django.db import models

DEPARTMENT_CHOICES = (
    ("anatomy","Anatomy"),
    ("physiology","Physiology"),
    ("biochemistry","Biochemistry"),
    ("general medicine","General Medicine"),
    ("general surgerys","General Surgery"),
    ("orthopaedics","Orthopaedics"),
    ("paediatrics","Paediatrics"),
    ("obstetrics & gynaecology","Obstetrics & Gynaecology"),
    ("ophthalmology","Ophthalmology"),
    ("otorhinolaryngology","Otorhinolaryngology"),
    ("dermatology","Dermatology"),
    ("anaesthesiology","Anaesthesiology"),
    ("psychiatry","Psychiatry"),
    ("radio diagnosis & imaging","Radio diagnosis & Imaging"),
    ("community medicine","Community Medicine"),
    ("pulmonary medicine","Pulmonary Medicine"),
    ("urology","Urology"),
    ("nephrology","Nephrology"),
    ("neuroscience","Neuroscience"),
    ("gastroenterology","Gastroenterology"),
    ("cardiology","Cardiology"),
    ("ctvs","CTVS"),
    ("endocrinology","Endocrinology"),
    ("oncology","Oncology")
)


class EquipmentRequest(models.Model):
    name = models.CharField(max_length = 200)
    department = models.CharField(max_length=200,choices = DEPARTMENT_CHOICES)
    designation = models.CharField(max_length=200)
    eqpname = models.CharField(max_length=200)
    fromDate = models.DateField()
    toDate = models.DateField()
    request_status = models.BooleanField(default=False,blank=True)
    message = models.TextField(blank=True)
    user_id = models. IntegerField(blank=True)

    def __str__(self):
        return self.name
