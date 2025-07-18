import json
from django.urls import reverse
from rest_framework.test import APITestCase
from firedata.models import *
from firedata.model_factories import *

class BurningEventTest(APITestCase):
    def setUp(self):
        # Cria um evento com ConservationUnit, que por sua vez cria ManagementUnit e RegionalGroup
        self.burning_event_1 = BurningEventFactory()
        self.burning_event_2 = BurningEventFactory(
            conservation_unit=self.burning_event_1.conservation_unit
        )

        self.list_url = reverse('burning_events_api')
        self.detail_url = reverse('burningevent_update', kwargs={'pk': self.burning_event_1.pk})

    def test_list_burning_events(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_burning_event_detail(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('wildfire_area', response.json())

    def test_update_burning_event(self):
        data = {
            "conservation_unit": self.burning_event_1.conservation_unit.pk,
            "wildfire_area": "30.0",
            "controlled_burn_area": "10.0",
            "firebreak_area": "20.0",
            "area_total": "60.0",  # 30 + 10 + 20 = 60
            "total_prevention_area": "25.0",
            "total_firefighting_area": "30.0",  # 25 + 30 = 55 <= 60
            "prescribed_burn_area": "0.0",
            "natural_fire_area": "0.0",
            "isolated_indigenous_area": "0.0",  
                }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.burning_event_1.refresh_from_db()
        self.assertEqual(float(self.burning_event_1.wildfire_area), 30.0)

    def test_delete_burning_event(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(BurningEvent.objects.filter(pk=self.burning_event_1.pk).exists())

    def test_create_burning_event(self):
        url = reverse('burningevent_create')
        data = {
            "conservation_unit": self.burning_event_1.conservation_unit.pk,
            "wildfire_area": "30.0",
            "controlled_burn_area": "10.0",
            "firebreak_area": "20.0",
            "area_total": "60.0",  # 30 + 10 + 20 = 60
            "total_prevention_area": "25.0",
            "total_firefighting_area": "30.0",  # 25 + 30 = 55 <= 60
            "prescribed_burn_area": "0.0",
            "natural_fire_area": "0.0",
            "isolated_indigenous_area": "0.0",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BurningEvent.objects.count(), 3)

class ConservationUnitTest(APITestCase):
    def setUp(self):
        self.unit = ConservationUnitFactory()
        self.list_url = reverse('conservation_unit_list')
        self.detail_url = reverse('conservation_unit_update', kwargs={'pk': self.unit.pk})
        self.create_url = reverse('conservation_unit_create')

    def test_list_units(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_get_unit_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.unit.name)

    def test_update_unit(self):
        data = {
            'name': 'Nova UC',
            'management_unit': self.unit.management_unit.pk,
            'regional_group': self.unit.regional_group.pk,
            'area_in_uc': 888.88,
            'percent_fire_affected_in_uc': 0.75
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.unit.refresh_from_db()
        self.assertEqual(str(self.unit.area_in_uc), '888.88')

    def test_delete_unit(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(ConservationUnit.objects.filter(pk=self.unit.pk).exists())

    def test_create_unit(self):
        new_unit = ConservationUnitFactory.create()
        assert new_unit.regional_group is not None  # security

        data = {
            'name': 'New UC Created',
            'management_unit': new_unit.management_unit.pk,
            'regional_group': new_unit.regional_group.pk,
            'area_in_uc': new_unit.area_in_uc,
            'percent_fire_affected_in_uc': new_unit.percent_fire_affected_in_uc
        }

class ManagementUnitTest(APITestCase):
    def setUp(self):
        self.management_unit = ManagementUnitFactory()
        self.list_url = reverse("management_unit_list")
        self.detail_url = reverse("management_unit", kwargs={'pk': self.management_unit.pk})
        self.create_url = reverse("management_unit_create")

    def test_list_management_units(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()),1)

    def test_get_management_unit_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.management_unit.name)

    def test_update_management_unit(self):
        data = {
            'name': 'APA Recife',
            'regional_group': self.management_unit.regional_group.pk
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.management_unit.refresh_from_db()
        self.assertEqual(str(self.management_unit.name), 'APA Recife')

    def test_delete_management_unit(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(ManagementUnit.objects.filter(pk=self.management_unit.pk).exists())

    def test_create_management_unit(self):
        new_unit = ManagementUnitFactory.create()
        assert new_unit.regional_group is not None
        data = {
            'name': 'APA Recife',
            'regional_group': new_unit.regional_group.pk
        }
