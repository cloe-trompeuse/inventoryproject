# Generated by Django 5.0.6 on 2024-05-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodName', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Stationery', 'Stationery'), ('Hygiene', 'Hygiene'), ('Electronics', 'Electronics')], max_length=30, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
