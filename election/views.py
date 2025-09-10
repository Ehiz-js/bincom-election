from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.http import JsonResponse
from .models import PollingUnit, AnnouncedPuResults, LGA, Ward, Party
from django.utils import timezone


def get_lgas(request, state_id):
    lgas = LGA.objects.filter(state_id=state_id).values("lga_id", "lga_name")
    return JsonResponse(list(lgas), safe=False)

def get_wards(request, lga_id):
    wards = Ward.objects.filter(lga_id=lga_id).values("ward_id", "ward_name")
    return JsonResponse(list(wards), safe=False)

def get_polling_units(request, ward_id):
    pus = PollingUnit.objects.filter(ward_id=ward_id).values("uniqueid", "polling_unit_name")
    return JsonResponse(list(pus), safe=False)

#Create your models here

def home(request):
    return render(request, "election/home.html")


#q1
def polling_unit_results(request):
    results = None
    selected_pu = None

    if request.method == "POST":
        pu_id = request.POST.get("polling_unit")
        if pu_id:
            selected_pu = get_object_or_404(PollingUnit, uniqueid=pu_id)
            results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=selected_pu)

    return render(request, "election/polling_unit_results.html", {
        "results": results,
        "selected_pu": selected_pu,
    })
  
#q2
def lga_results(request):
    totals = None
    if request.method == "POST":
        lga_id = request.POST.get("lga")
        lga = get_object_or_404(LGA, lga_id=lga_id)
        totals = (
            AnnouncedPuResults.objects
            .filter(polling_unit_uniqueid__lga_id=lga.lga_id)
            .values("party_abbreviation")
            .annotate(total_score=Sum("party_score"))
            .order_by("-total_score")
        )
    return render(request, "election/lga_results.html", {"totals": totals})
  
#q3
def add_polling_unit_results(request):
    if request.method == "POST":
        pu_name = request.POST.get("pu_name")
        ward_id = request.POST.get("ward_id")
        lga_id = request.POST.get("lga_id")

        last_pu = PollingUnit.objects.order_by("-polling_unit_id").first()
        next_pu_id = (last_pu.polling_unit_id + 1) if last_pu else 1
        
        new_pu = PollingUnit.objects.create(
            polling_unit_id=next_pu_id,
            ward_id=ward_id,
            lga_id=lga_id,
            polling_unit_name=pu_name,
            entered_by_user='test_user',
            date_entered=timezone.now(),
            user_ip_address='127.0.0.1'
        )

        for party in Party.objects.all():
            score = request.POST.get(f"score_{party.partyid}")
            AnnouncedPuResults.objects.create(
                polling_unit_uniqueid=new_pu,
                party_abbreviation=party.partyid[:4],
                party_score=int(score or 0),
                entered_by_user="test_user",
                date_entered=timezone.now(),
                user_ip_address = '127.0.0.1'
            )

        return redirect("polling_unit_results")

    parties = Party.objects.all()
    return render(request, "election/add_polling_unit_results.html", {
        "parties": Party.objects.all(),
        "lgas": LGA.objects.all(),
        "wards": Ward.objects.all(),
    })
  

