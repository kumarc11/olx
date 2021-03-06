# Generated by Django 3.1.7 on 2021-05-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('image', models.ImageField(max_length=255, upload_to='pics/%y/%m/%d')),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=50)),
                ('teacher_class', models.CharField(choices=[('btechcse1', 'BTech(CSE) 1st Sem'), ('btechcse2', 'BTech(CSE) 2nd Sem'), ('btechcse3', 'BTech(CSE) 3rd Sem'), ('btechcse4', 'BTech(CSE) 4th Sem'), ('btechcse5', 'BTech(CSE) 5th Sem'), ('btechcse6', 'BTech(CSE) 6th Sem')], max_length=50)),
                ('dob', models.DateField()),
                ('married', models.BooleanField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('video_length', models.DecimalField(decimal_places=1, max_digits=6)),
            ],
        ),
    ]
