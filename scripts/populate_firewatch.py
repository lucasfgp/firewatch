import os
import sys
import django
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) 
PROJECT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..')) 
sys.path.append(PROJECT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firewatch.settings')
django.setup()

from firedata.models import *

CSV_PATH = os.path.join(PROJECT_DIR, 'data', 'burned_areas_env_preservation_area2024.csv')

def parse_float(value):
    try:
        return float(value.strip().replace('.', '').replace(',', '.') or 0)
    except (ValueError, AttributeError):
        return 0

def parse_decimal(value):
    try:
        return Decimal(value.strip().replace('.', '').replace(',', '.'))
    except (InvalidOperation, AttributeError):
        return Decimal('0.00')

with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    header = next(csv_reader)  # Skip header

    for row in csv_reader:
        if row[0].strip() == 'TOTAL':
            continue
        # row indices:
        # 0 = Unidade de Conservação
        # 1 = NGI
        # 2 = GR
        # 3 = Incêndio (ha)
        # 4 = Queima prescrita (ha)
        # 5 = Queima controlada (ha)
        # 6 = Aceiro (ha)
        # 7 = Fogo natural (ha)
        # 8 = Indígenas isolados (ha)
        # 9 = Total Prevenção (ha)
        # 10 = Total Combate (ha)
        # 11 = Área TOTAL (ha)
        # 12 = Área UC (ha)
        # 13 = % de AAF na UC

        # the get_or_create method creates a new object if it doesn't exist
        # and returns a tuple (object, created)
        # where 'created' is a boolean indicating if the object was created
        # so, it SELECTS and then INSERTS

        rg_name = row[2].strip()
        regional_group, _ = RegionalGroup.objects.get_or_create(name=rg_name)
        uc_name = row[0].strip()
        uc_type_name = uc_name.split()[0].strip().upper()

        # add ngi " "
        management_unit_name = row[1].strip()
        management_unit, _ = ManagementUnit.objects.get_or_create(
        name=management_unit_name,
        regional_group=regional_group,
        )

        uc_area_in_uc = row[12].strip()

        uc, _ = ConservationUnit.objects.get_or_create(
            name=uc_name,
            regional_group=regional_group,
            management_unit=management_unit,
        )
        
        uc.area_in_uc = parse_decimal(row[12])
        percent_fire_affected_in_uc = parse_decimal(row[13])
        uc.percent_fire_affected_in_uc = percent_fire_affected_in_uc
        uc.save()

        event = BurningEvent.objects.create(
            conservation_unit=uc,
            wildfire_area=parse_float(row[3]),
            prescribed_burn_area=parse_float(row[4]),
            controlled_burn_area=parse_float(row[5]),
            firebreak_area=parse_float(row[6]),
            natural_fire_area=parse_float(row[7]),
            isolated_indigenous_area=parse_float(row[8]),
            total_prevention_area=parse_float(row[9]),
            total_firefighting_area=parse_float(row[10]),
            area_total=parse_float(row[11]),
        )
