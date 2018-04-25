# Generated by Django 2.0.4 on 2018-04-25 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0019_delete_active_hour_reload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume_Day_Week_Dont_Win',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monday_day', models.BooleanField(default=False)),
                ('Tuesday_day', models.BooleanField(default=False)),
                ('Wednesday_day', models.BooleanField(default=False)),
                ('Thursday_day', models.BooleanField(default=False)),
                ('Friday_day', models.BooleanField(default=False)),
                ('Saturday_day', models.BooleanField(default=False)),
                ('Sunday_day', models.BooleanField(default=False)),
                ('app', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_data.EB_App')),
            ],
            options={
                'verbose_name': 'Резюме - дни недели (Не максимальные)',
                'verbose_name_plural': 'Резюме - дни недели (Не максимальные)',
            },
        ),
        migrations.CreateModel(
            name='Resume_Day_Week_Win',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monday_day', models.BooleanField(default=False)),
                ('Tuesday_day', models.BooleanField(default=False)),
                ('Wednesday_day', models.BooleanField(default=False)),
                ('Thursday_day', models.BooleanField(default=False)),
                ('Friday_day', models.BooleanField(default=False)),
                ('Saturday_day', models.BooleanField(default=False)),
                ('Sunday_day', models.BooleanField(default=False)),
                ('app', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_data.EB_App')),
            ],
            options={
                'verbose_name': 'Резюме - дни недели (Максимальные)',
                'verbose_name_plural': 'Резюме - дни недели (Максимальные)',
            },
        ),
        migrations.CreateModel(
            name='Resume_Hour_Dont_Win',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_hour', models.IntegerField(default=0)),
                ('app', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_data.EB_App')),
                ('day', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_data.Resume_Day_Week_Dont_Win')),
            ],
            options={
                'verbose_name': 'Резюме - активные часы (Не максимальные)',
                'verbose_name_plural': 'Резюме - активные часы (Не максимальные)',
            },
        ),
        migrations.CreateModel(
            name='Resume_Hour_Win',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_hour', models.IntegerField(default=0)),
                ('app', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_data.EB_App')),
                ('day', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_data.Resume_Day_Week_Win')),
            ],
            options={
                'verbose_name': 'Резюме - активные часы (Максимальные)',
                'verbose_name_plural': 'Резюме - активные часы (Максимальные)',
            },
        ),
    ]