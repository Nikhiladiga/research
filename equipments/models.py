from django.db import models  

DEPARTMENT_CHOICES = (
    ('anatomy','Anatomy'),
    ('physiology','Physiology'),
    ('biochemistry','Biochemistry'),
    ('general medicine','General Medicine'),
    ('general surgerys','General Surgery'),
    ('orthopaedics','Orthopaedics'),
    ('paediatrics','Paediatrics'),
    ('obstetrics & gynaecology','Obstetrics & Gynaecology'),
    ('ophthalmology','Ophthalmology'),
    ('otorhinolaryngology(ENT)','Otorhinolaryngology(ENT)'),
    ('dermatology','Dermatology'),
    ('anaesthesiology','Anaesthesiology'),
    ('psychiatry','Psychiatry'),
    ('radio diagnosis & imaging','Radio diagnosis & Imaging'),
    ('community medicine','Community Medicine'),
    ('pulmonary medicine','Pulmonary Medicine'),
    ('urology','Urology'),
    ('nephrology','Nephrology'), 
    ('neuroscience','Neuroscience'),
    ('gastroenterology','Gastroenterology'),
    ('cardiology','Cardiology'),
    ('ctvs','CTVS'),
    ('endocrinology','Endocrinology'),
    ('oncology','Oncology')
)

INSTITUTION_CHOICES = (
    ('ks hegde medical academy','KS HEGDE MEDICAL ACADEMY'),
    ('nmam insitute of technology','NMAM INSTITUTE OF TECHNOLOGY'),
    ('nitte institue of communication','NITTE INSTITUTE OF COMMUNICATION')
)

STATUS_CHOICES = (
    ('available','AVAILABLE'),
    ('not available','NOT AVAILABLE'),
    ('under maintenance',"UNDER MAINTENANCE")
)

class Equipment(models.Model):
    id = models.AutoField(primary_key=True,)
    Equipment_Name = models.CharField(max_length = 200,unique = True)
    Incharge_ID = models.CharField(max_length = 200)
    Department = models.CharField(max_length = 200,choices =DEPARTMENT_CHOICES)
    Institution = models.CharField(max_length = 200,choices=INSTITUTION_CHOICES,default='ks hegde medical academy')
    Status = models.CharField(max_length = 200,default='available',choices = STATUS_CHOICES)
    Product_ID = models.CharField(max_length = 200)
    Company = models.CharField(max_length = 200)
    Utilities= models.TextField(blank=True)
    Consumables=  models.TextField(blank=True)
    image_main= models.ImageField(upload_to='photos/%Y%m%d/') 

    def __str__(self):
        return str(self.id)
