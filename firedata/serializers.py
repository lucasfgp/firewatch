from rest_framework import serializers
from decimal import Decimal
from .models import *

class RegionalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionalGroup
        fields = ['id', 'name']

class ManagementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementUnit
        fields = '__all__'

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

class ConservationUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConservationUnit
        fields = '__all__'

    def validate_percent_fire_affected_in_uc(self, value):
        if not 0 <= value <= 100:
            raise serializers.ValidationError("Percent must be between 0 and 100.")
        return value

class BurningEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BurningEvent
        fields = '__all__'

    def validate_area_total(self, value):
        # Converte as áreas da requisição para Decimal
        wildfire_area = Decimal(self.initial_data.get('wildfire_area', 0) or 0)
        controlled_burn_area = Decimal(self.initial_data.get('controlled_burn_area', 0) or 0)
        firebreak_area = Decimal(self.initial_data.get('firebreak_area', 0) or 0)

        total_sum = wildfire_area + controlled_burn_area + firebreak_area

        if abs(value - total_sum) > Decimal("0.01"):
            raise serializers.ValidationError("The sum of partial areas does not correspond to the total area.")
        
        return value

    def validate(self, data):
        if data['total_prevention_area'] + data['total_firefighting_area'] > data['area_total']:
            raise serializers.ValidationError("Sum of prevention and firefighting areas can't exceed total area.")
        return data  

class BurningEventListSerializer(serializers.ModelSerializer):
    conservation_unit_name = serializers.CharField(source='conservation_unit.name', read_only=True)
    class Meta:
        model = BurningEvent
        fields = ['id', 'conservation_unit_name', 'wildfire_area', 'prescribed_burn_area', 'controlled_burn_area', 
                  'firebreak_area', 'natural_fire_area', 'isolated_indigenous_area', 'area_total', 
                  'total_prevention_area', 'total_firefighting_area']
        read_only_fields = ['id']
