# Generated by Django 3.2.5 on 2023-10-25 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('phno', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Heroines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heroin_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_cost', models.BigIntegerField(default=0)),
                ('movie_director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.director')),
                ('movie_hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.heroes')),
                ('movie_heroin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.heroines')),
            ],
        ),
        migrations.CreateModel(
            name='BookMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_seats', models.IntegerField(default=0)),
                ('seat_no', models.CharField(max_length=50)),
                ('total_cost', models.IntegerField(default=0)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.customer')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.movie')),
            ],
        ),
    ]
