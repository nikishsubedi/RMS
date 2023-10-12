# Generated by Django 4.2.5 on 2023-10-12 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0007_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='foods', to='rms.category'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'PENDING'), ('CO', 'COOKING'), ('CA', 'CANCELLED'), ('C', 'COMPLETED')], default='P', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'FEMALE')], max_length=1),
        ),
    ]
