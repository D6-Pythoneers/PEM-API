from django.db import models

# Create your models here.
class Assesment(models.Model):
    assesment_id = models.AutoField(primary_key=True)
    evaluation = models.ForeignKey('Evaluations', blank=True, null=True,on_delete=models.DO_NOTHING(None,None,None,None))
    cat = models.ForeignKey('Assesmentcategories', blank=True, null=True,on_delete=models.DO_NOTHING(None,None,None,None))
    indicator = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    first_evaluation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    final_evaluation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Assesment'
