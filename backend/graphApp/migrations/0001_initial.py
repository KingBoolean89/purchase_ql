# Generated by Django 3.0.5 on 2020-05-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Segement', models.CharField(max_length=150)),
                ('Country', models.CharField(max_length=150)),
                ('Product', models.CharField(max_length=150)),
                ('Units', models.IntegerField()),
                ('Sales', models.IntegerField()),
                ('Datesold', models.CharField(max_length=150)),
            ],
        ),
    ]