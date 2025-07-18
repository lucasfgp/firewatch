from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('api/burningeventslist/', api.BurningEventList.as_view(), name='burning_events_api'),
    path('api/conservationunitlist/', api.ConservationUnitList.as_view(), name='conservation_unit_list'),
    path('api/regionalgrouplist/', api.RegionalGroupList.as_view(), name='regional_group_list'),
    path('api/burningevents/create', api.BurningEventCreate.as_view(), name='burningevent_create'),
    path('api/burningevents/<int:pk>', api.BurningEventDetails.as_view(), name='burningevent_update'),
    path('api/conservationunit/create', api.ConservationUnitCreate.as_view(), name='conservation_unit_create'),
    path('api/conservationunit/<int:pk>', api.ConservationUnitDetails.as_view(), name='conservation_unit_update'),
    path('api/managementunitlist/', api.ManagamentUnitList.as_view(), name='management_unit_list'),
    path('api/managementunit/create', api.ManagementUnitCreate.as_view(), name='management_unit_create'),
    path('api/managementunit/<int:pk>', api.ManagementUnitDetails.as_view(), name='management_unit'),

]