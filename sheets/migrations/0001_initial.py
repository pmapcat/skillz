# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_level', models.IntegerField(db_index=True, verbose_name='\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430\u0432\u044b\u043a\u0430')),
                ('previous_categories', models.ManyToManyField(blank=True, to='sheets.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='SkillInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_instances', to='sheets.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='\u0422\u0438\u043f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
            ],
        ),
        migrations.CreateModel(
            name='SpreadSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.CharField(db_index=True, max_length=1000, verbose_name='\u0418\u043c\u044f \u0440\u0435\u0431\u0435\u043d\u043a\u0430')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='\u0412\u043e\u0437\u0440\u0430\u0441\u0442')),
            ],
        ),
        migrations.AddField(
            model_name='skillinstance',
            name='spreadsheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_instances', to='sheets.SpreadSheet'),
        ),
        migrations.AddField(
            model_name='skill',
            name='taxonomy_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='sheets.SkillType'),
        ),
    ]
