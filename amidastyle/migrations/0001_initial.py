# Generated by Django 4.1.4 on 2023-02-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=256)),
                ('account_id', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=256)),
                ('subscription', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=100)),
                ('contacts', models.CharField(max_length=256)),
                ('price', models.PositiveIntegerField()),
                ('account_id', models.PositiveIntegerField()),
            ],
        ),
    ]
