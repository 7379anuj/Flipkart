# Generated by Django 4.2.1 on 2023-05-25 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_rename_coustemers_coustomers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coustomers',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CoustemersAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=15, null=True)),
                ('street_number', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('Coustomers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.coustomers')),
            ],
        ),
    ]
