# Generated by Django 5.0.3 on 2024-04-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_player_teams_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
