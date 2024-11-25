# Generated by Django 5.1.1 on 2024-11-22 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator_app', '0010_passenger_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Passenger_Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id1', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='passenger_reg',
            name='category',
            field=models.CharField(default='General', max_length=100),
        ),
        migrations.AddField(
            model_name='passenger_reg',
            name='package',
            field=models.CharField(default='Standard', max_length=100),
        ),
    ]
