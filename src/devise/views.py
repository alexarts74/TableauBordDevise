from django.shortcuts import render, HttpResponse
import api
# Create your views here.
def dashboard(request, days=60, currencies="EUR"):
    days, rates = api.get_rates(currencies=currencies.split(","), days = days)
    return render(request, "devise/index.html", context={"rates": rates, "days": days})
