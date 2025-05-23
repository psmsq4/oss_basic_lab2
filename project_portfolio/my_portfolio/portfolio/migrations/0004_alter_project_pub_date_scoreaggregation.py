# Generated by Django 5.2 on 2025-05-04 11:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 4, 11, 28, 32, 478564, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='ScoreAggregation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_scores', models.IntegerField(default=0)),
                ('total_votes', models.IntegerField(default=0)),
                ('average_scores', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project')),
            ],
        ),
    ]
