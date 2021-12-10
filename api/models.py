from django.db import models
from django.contrib.auth import get_user_model
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
    user = models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING)
    evaluated = models.BooleanField()
    academic_year = models.DateTimeField()
    created_by = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    max_score = models.IntegerField()
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Evaluations'

class Goals(models.Model):
    goal_id = models.AutoField(primary_key=True)
    evaluation = models.ForeignKey(Evaluations,on_delete=models.DO_NOTHING)
    goal = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    goal_result = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    max_score = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        db_table = 'Goals'

class Recommendations(models.Model):
    recommender_id = models.AutoField(primary_key=True)
    evaluation = models.ForeignKey(Evaluations,on_delete=models.DO_NOTHING)
    recommendation = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        db_table = 'Recommendations'

class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'Roles'

class Schools(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_manager = models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING, db_column='school_manager')
    school_name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    evaluated = models.BooleanField(blank=True, null=True)
    academic_year = models.DateTimeField()

    class Meta:
        db_table = 'Schools'

class Subcategories(models.Model):
    sub_cat_id = models.AutoField(primary_key=True)
    cat = models.ForeignKey(Assesmentcategories,on_delete=models.DO_NOTHING)
    sub_cat = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        db_table = 'SubCategories'
