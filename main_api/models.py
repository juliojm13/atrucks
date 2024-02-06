from django.db import models


class OpenData(models.Model):
    code = models.IntegerField(verbose_name='Code number')
    from_limit = models.IntegerField(verbose_name='From limit')
    to_limit = models.IntegerField(verbose_name='To limit')
    capacity = models.IntegerField(verbose_name='Capacity')
    operator = models.CharField(verbose_name='Numbers operator', max_length=500)
    region = models.CharField(verbose_name='Region', max_length=500)
    inn = models.CharField(verbose_name='INN', max_length=500)

    class Meta:
        db_table = 'open_data'
