# Generated by Django 5.0.6 on 2024-06-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningapp', '0007_remove_profile_id_profile_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistrations',
            name='user_image',
            field=models.ImageField(default=1, upload_to='profiles'),
            preserve_default=False,
        ),
    ]
