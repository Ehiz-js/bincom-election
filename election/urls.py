from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("polling-unit/", views.polling_unit_results, name="polling_unit_results"),
    path("lga-total/", views.lga_results, name="lga_results"),
    path("add-results/", views.add_polling_unit_results, name="add_polling_unit_results"),

    # API endpoints
    path("api/lgas/<int:state_id>/", views.get_lgas, name="get_lgas"),
    path("api/wards/<int:lga_id>/", views.get_wards, name="get_wards"),
    path("api/pus/<int:ward_id>/", views.get_polling_units, name="get_polling_units"),
]
