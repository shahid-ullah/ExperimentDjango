# Generated by Django 3.1.3 on 2020-11-10 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0003_hero_headshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='not_editable_field',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=200),
            preserve_default=False,
        ),
    ]
