from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
	port = Portfolio.objects.all()

	return render(request, 'portfolio.html', {"port":port})
