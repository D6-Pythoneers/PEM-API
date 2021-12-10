from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Assesment(models.Model):
    assesment_id = models.AutoField(primary_key=True)
    evaluation = models.ForeignKey('Evaluations', blank=True, null=True,on_delete=models.DO_NOTHING())
    cat = models.ForeignKey('Assesmentcategories', blank=True, null=True,on_delete=models.DO_NOTHING())
    indicator = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    first_evaluation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    final_evaluation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Assesment'
