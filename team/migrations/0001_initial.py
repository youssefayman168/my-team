# Generated by Django 4.2.1 on 2023-06-10 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Memeber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=255)),
                ('posistion', models.CharField(max_length=120)),
                ('phone_number', models.PositiveBigIntegerField()),
                ('picture', models.ImageField(upload_to='images/team/')),
                ('email', models.EmailField(max_length=254)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.section')),
                ('skills', models.ManyToManyField(to='team.skill')),
            ],
        ),
    ]