from django.db import models

# Create your models here.

class Director(models.Model):
    director_name = models.CharField(max_length=150)

    def __str__(self):
        return self.director_name

class Heroes(models.Model):
    hero_name = models.CharField(max_length=150)

    def __str__(self):
        return self.hero_name

class Heroines(models.Model):
    heroin_name = models.CharField(max_length=150)

    def __str__(self):
        return self.heroin_name

class Theater(models.Model):
    theater_name = models.CharField(max_length=250,default=None)

    def __str__(self):
        return self.theater_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_director = models.ForeignKey(Director,on_delete=models.CASCADE)
    movie_hero = models.ForeignKey(Heroes,on_delete=models.CASCADE)
    movie_heroin = models.ForeignKey(Heroines,on_delete=models.CASCADE)
    movie_cost=  models.BigIntegerField(default=0)
    movie_poster = models.ImageField(upload_to='images/',default=None)

    def __str__(self):
        return self.movie_name

class ShowTime(models.Model):
    movie_data = models.ForeignKey(Movie,on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    # def __str__(self):
    #     return f"{self.datetime}"


class Customer(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phno = models.BigIntegerField(default=0)
    password = models.CharField(max_length=150,default=None)

    def __str__(self):
        return self.fname

class BookMovie(models.Model):
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    no_of_seats = models.IntegerField(default=0)
    seat_no = models.CharField(max_length=50)
    total_cost = models.IntegerField(default=0)
    show_time = models.ForeignKey(ShowTime,on_delete=models.CASCADE,default=None)
    booking_status = models.BooleanField(default=False)





