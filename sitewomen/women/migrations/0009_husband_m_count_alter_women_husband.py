# Generated by Django 4.2.1 on 2024-03-07 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0008_husband_women_husband'),
    ]

    operations = [
        migrations.AddField(
            model_name='husband',
            name='m_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='women',
            name='husband',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='woman', to='women.husband'),
        ),
    ]
