from django.shortcuts import render, redirect
import api
# Create your views here.
def dashboard(request, days_range=30, currencies="EUR"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "personnalisé")
    return render(request, "devise/index.html", context={"rates": rates, "days": days, "currencies":currencies, "page_label": page_label})


def redirect_home(request):
    return redirect("home", days_range=30, currencies="EUR")
