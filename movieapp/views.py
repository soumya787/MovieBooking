import re

from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from movieapp.models import *
# Create your views here.
def addmovie_fun(request):
    if request.method =='POST':
        m1 = Movie()
        m1.movie_name = request.POST['txtMovieName']
        m1.movie_hero =Heroes.objects.get(hero_name=request.POST['ddlHero'])
        m1.movie_heroin = Heroines.objects.get(heroin_name=request.POST['ddlHeroin'])
        m1.movie_director = Director.objects.get(director_name = request.POST['ddlDirector'])
        m1.movie_cost = int(request.POST['txtCost'])
        m1.movie_poster  =request.POST['txtFile']
        m1.save()
        return render(request,'admin/addmovie.html')
    else:
        director_data  = Director.objects.all()
        hero_data = Heroes.objects.all()
        heroin_data = Heroines.objects.all()
        return render(request,'admin/addmovie.html',
                      {'Director':director_data,
                       'Hero':hero_data,'Heroin':heroin_data
                       })


def displaymovie_fun(request):
    data = Movie.objects.all()
    return render(request,'admin/displaymovie.html',{'Movie':data})


def reg_fun(request):
    if request.method == 'POST':
        c1 = Customer()
        c1.fname = request.POST['txtFname']
        c1.lname = request.POST['txtLname']
        c1.phno = int(request.POST['txtPhno'])
        c1.email = request.POST['txtMail']
        c1.password = request.POST['txtPswd']
        if Customer.objects.filter(Q(fname=request.POST['txtFname']) & Q(password=request.POST['txtPswd'])).exists():
            return render(request,'customer/registerpage.html',{'msg':'UserName is alreday exists try another'})
        else:
            c1.save()
            return render(request,'login.html')
    else:
        return render(request,'customer/registerpage.html')


def log_fun(request):
    if request.method == 'POST':
        username = request.POST['txtUname']
        password = request.POST['txtPswd']
        if Customer.objects.filter(Q(fname=username) & Q(password=password)).exists():
            request.session['Name'] = username
            request.session['usertype'] = 'Customer'
            return redirect('home')
        else:
            u1 = authenticate(username=username,password=password)
            if u1 is not None:
                if u1.is_superuser:
                    request.session['usertype'] = 'Admin'
                    return render(request,'admin/home.html')

            return redirect('log')
    else:
        return render(request,'login.html')

def showtime_fun(request):
    if request.method=='POST':
        s1 = ShowTime()
        s1.movie_data = Movie.objects.get(movie_name=request.POST['ddlMovies'])
        s1.theater = Theater.objects.get(theater_name= request.POST['ddlTheater'])
        s1.date_time = request.POST['txtDateTime']
        s1.save()
        return redirect('showtime')
    else:
        m1 = Movie.objects.all()
        t1 = Theater.objects.all()
        return render(request,'admin/showtime.html',
                      {'Movie':m1,'Theater':t1})

def bookingdetails_fun(request):
    b1 = BookMovie.objects.all()
    return render(request,'admin/bookingdetails.html',{'data':b1})

def updatestatus(request,id):
    b1 = BookMovie.objects.get(id=id)
    b1.booking_status = True
    b1.save()
    return redirect('bookingdetails')

# Customer home page
def home_fun(request):
    if request.session['usertype'] == 'Customer':
        return render(request,'customer/home.html',{'data' : request.session['Name']})
    else:
        return render(request,'admin/home.html')


def showdata_fun(request):
    s1 = ShowTime.objects.all()
    return render(request,'customer/movieshows.html',{'Show':s1})


def bookshow_fun(request,showid):
    s1 = ShowTime.objects.get(id=showid)
    booked_seats = []  # Replace with actual data
    selected_seats = None
    if request.method == 'POST':
        selected_seats = request.POST['selected_seats']
        booked_seats = re.split(',',selected_seats)
        # booked_seats.append(x)

        b1 = BookMovie()
        b1.movie_id = Movie.objects.get(id = s1.movie_data_id)
        b1.show_time = ShowTime.objects.get(id=showid)
        b1.seat_no = selected_seats
        b1.no_of_seats  = len(booked_seats)
        b1.customer_id = Customer.objects.get(fname = request.session['Name'])
        m1 = Movie.objects.get(id = s1.movie_data_id)
        b1.total_cost = m1.movie_cost * len(booked_seats)
        b1.save()
        return redirect('showdata')
    else:
        row = ['A', 'B', 'C', 'D', 'E']  # Replace with actual data
        available_seats1 = ['1','2','3','4','5','6','7','8','9','10']
        available_seats = [[i+j for j in available_seats1] for i in row ]
        print(available_seats)

        status = [True,False]
        b1 = BookMovie.objects.values()
        for i in range(len(b1)):
           print(i)
           booked_seats.append(re.split(',',b1[i]['seat_no']))

        print(booked_seats)
        booked_seat = []
        for i in range(len(booked_seats)):
            for j in range(len(booked_seats[i])):
                booked_seat.append(booked_seats[i][j])
        print(booked_seat)

        return render(request, 'customer/bookmovie.html', {
            'available_seats': available_seats,
            'booked_seats': booked_seat,
            'row' : row,
            'status':status
        })


def cancel_booking(request,id):
    b1 = BookMovie.objects.get(id=id)
    b1.delete()
    return redirect('bookingdetails')