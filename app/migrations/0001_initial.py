# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-10 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет')),
                ('color_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Код цвета')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100, null=True, verbose_name='Название больницы')),
                ('hospital_adress', models.CharField(max_length=100, null=True, verbose_name='Адрес')),
                ('hospital_number1', models.CharField(max_length=25, null=True, verbose_name='Номер1')),
                ('hospital_number2', models.CharField(max_length=25, null=True, verbose_name='Номер2')),
                ('lat', models.CharField(max_length=25, null=True, verbose_name='Lat')),
                ('lng', models.CharField(max_length=25, null=True, verbose_name='Lng')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('fam', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('gender', models.CharField(blank=True, max_length=40, null=True, verbose_name='Пол')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='Рост')),
                ('body', models.CharField(blank=True, max_length=40, null=True, verbose_name='Телосложение')),
                ('eyes_color', models.CharField(blank=True, max_length=40, null=True, verbose_name='Цвет глаз')),
                ('hair_color', models.CharField(blank=True, max_length=40, null=True, verbose_name='Цвет волос')),
                ('shramy', models.BooleanField(default=False, verbose_name='Шрамы')),
                ('tatu', models.BooleanField(default=False, verbose_name='Тату')),
                ('protez', models.BooleanField(default=False, verbose_name='Протезы')),
                ('konech', models.BooleanField(default=False, verbose_name='Отсутсвие конечностей')),
                ('hat', models.CharField(blank=True, max_length=40, null=True, verbose_name='Головной убор')),
                ('vverh', models.CharField(blank=True, max_length=40, null=True, verbose_name='Верхняя одежда')),
                ('niz', models.CharField(blank=True, max_length=40, null=True, verbose_name='Штаны')),
                ('boots', models.CharField(blank=True, max_length=40, null=True, verbose_name='Обувь')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('city', models.CharField(blank=True, max_length=40, null=True, verbose_name='Город')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('boots_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Color', verbose_name='Цвет обуви')),
                ('hat_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Color', verbose_name='Цвет головного убора')),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Hospital', verbose_name='Больница')),
                ('niz_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Color', verbose_name='Цвет нижней одежды')),
                ('vverh_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Color', verbose_name='Цвет верхней одежды')),
            ],
        ),
        migrations.CreateModel(
            name='Post_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('fam', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('gender', models.CharField(blank=True, max_length=40, null=True, verbose_name='Пол')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='Рост')),
                ('body', models.CharField(blank=True, max_length=40, null=True, verbose_name='Телосложение')),
                ('eyes_color', models.CharField(blank=True, max_length=40, null=True, verbose_name='Цвет глаз')),
                ('hair_color', models.CharField(blank=True, max_length=40, null=True, verbose_name='Цвет волос')),
                ('shramy', models.BooleanField(default=False, verbose_name='Шрамы')),
                ('tatu', models.BooleanField(default=False, verbose_name='Тату')),
                ('protez', models.BooleanField(default=False, verbose_name='Протезы')),
                ('konech', models.BooleanField(default=False, verbose_name='Отсутсвие конечностей')),
                ('image', models.ImageField(blank=True, default=False, upload_to='photos/%Y/%m/%d/')),
                ('hat', models.CharField(blank=True, max_length=40, null=True, verbose_name='Головной убор')),
                ('vverh', models.CharField(blank=True, max_length=40, null=True, verbose_name='Верхняя одежда')),
                ('niz', models.CharField(blank=True, max_length=40, null=True, verbose_name='Штаны')),
                ('boots', models.CharField(blank=True, max_length=40, null=True, verbose_name='Обувь')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адресс')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('city', models.CharField(blank=True, max_length=40, null=True, verbose_name='Город')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('boots_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Color', verbose_name='Цвет обуви')),
                ('hat_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Color', verbose_name='Цвет головного убора')),
                ('niz_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Color', verbose_name='Цвет нижней одежды')),
                ('vverh_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Color', verbose_name='Цвет верхней одежды')),
            ],
        ),
        migrations.AddField(
            model_name='comment_user',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.Post_user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.Post'),
        ),
    ]
