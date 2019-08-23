# Generated by Django 2.2.3 on 2019-08-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankBranches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('bank_id', models.IntegerField(blank=True, null=True)),
                ('branch', models.CharField(blank=True, max_length=74, null=True)),
                ('address', models.CharField(blank=True, max_length=195, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=26, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=49, null=True)),
            ],
            options={
                'db_table': 'bank_branches',
                'managed': False,
            },
        ),
    ]