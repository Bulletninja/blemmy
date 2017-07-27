# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('picture_url', models.URLField(blank=True)),
                ('translate_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('picture_url', models.URLField(blank=True)),
                ('type_of_dish_quantity', models.CharField(blank=True, choices=[('Gericht', 'Gericht'), ('Suppe', 'Suppe'), ('Dessert', 'Dessert'), ('...', '...')], max_length=2, null=True)),
                ('step_1', models.CharField(max_length=500)),
                ('step_2', models.CharField(max_length=500)),
                ('step_3', models.CharField(max_length=500)),
                ('step_4', models.CharField(max_length=500)),
                ('is_spicy', models.BooleanField(default=False, help_text='Ist diese Gericht Scharf?', verbose_name='Scharf')),
                ('is_vegi', models.BooleanField(default=False, help_text='Ist diese Gericht Vegi?', verbose_name='Vegi')),
            ],
        ),
        migrations.CreateModel(
            name='Wochen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jahr_quantity', models.CharField(blank=True, choices=[('2017', '2017'), ('2018', '2018')], max_length=2, null=True, verbose_name='Jahr')),
                ('woche_quantity', models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53')], max_length=2, null=True, verbose_name='Woche')),
                ('tag_quantity', models.CharField(blank=True, choices=[('Mo', 'Mo'), ('Di', 'Di'), ('Mi', 'Mi'), ('Do', 'Do'), ('Fr', 'Fr')], max_length=2, null=True, verbose_name='Tag')),
                ('menu_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_1+', to='cultinadb.Menue')),
                ('menu_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_2+', to='cultinadb.Menue')),
                ('menu_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_3+', to='cultinadb.Menue')),
                ('menu_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_4+', to='cultinadb.Menue')),
                ('tages_dessert', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tages_dessert+', to='cultinadb.Menue', verbose_name='Tagesdessert')),
                ('tages_suppe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tages_suppe+', to='cultinadb.Menue', verbose_name='Tagessuppe')),
                ('wochen_spezialitaet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wochen_spezialitaet+', to='cultinadb.Menue', verbose_name='Wochenspezialität')),
            ],
        ),
    ]
