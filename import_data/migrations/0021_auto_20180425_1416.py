# Generated by Django 2.0.4 on 2018-04-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0020_resume_day_week_dont_win_resume_day_week_win_resume_hour_dont_win_resume_hour_win'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume_hour_dont_win',
            old_name='active_hour',
            new_name='hour_end',
        ),
        migrations.RenameField(
            model_name='resume_hour_win',
            old_name='active_hour',
            new_name='hour_end',
        ),
        migrations.AddField(
            model_name='resume_hour_dont_win',
            name='hour_start',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resume_hour_win',
            name='hour_start',
            field=models.IntegerField(default=0),
        ),
    ]
