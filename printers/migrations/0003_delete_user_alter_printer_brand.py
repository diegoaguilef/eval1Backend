# Generated by Django 4.1.2 on 2022-12-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='printer',
            name='brand',
            field=models.CharField(choices=[['hp', 'HP'], ['brother', 'Brother'], ['cannon', 'Cannon'], ['lg', 'LG'], ['samsung', 'Samsung']], max_length=20),
        ),
    ]
