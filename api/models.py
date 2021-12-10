from django.db import models

# Create your models here.
class Assesment(models.Model):
    assesment_id = models.AutoField(primary_key=True)
    evaluation = models.ForeignKey('Evaluations', blank=True, null=True,on_delete=models.DO_NOTHING)
    cat = models.ForeignKey('Assesmentcategories', blank=True, null=True,on_delete=models.DO_NOTHING)
    indicator = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    first_evaluation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    final_evaluation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Assesment'

class Assesmentcategories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'AssesmentCategories'

class Evaluations(models.Model):
    evaluation_id = models.AutoField(primary_key=True)
    school = models.ForeignKey('Schools',on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User',on_delete=models.DO_NOTHING)
    evaluated = models.BooleanField()
    academic_year = models.DateTimeField()
    created_by = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    max_score = models.IntegerField()
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Evaluations'
