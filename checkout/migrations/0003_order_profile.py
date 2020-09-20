# Generated by Django 3.1 on 2020-09-18 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('checkout', '0002_auto_20200911_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='accounts.profile'),
        ),
    ]