from django.db import models

# Create your models here.

# Hierarchy of models:
# RegionalGroup
# └── ManagementUnit
#     └── ConservationUnit
#           └── BurningEvent
#              └── categories (ManyToManyField)  

class RegionalGroup(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name if self.name else "Unnamed Regional Group"
    
class ManagementUnit(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    regional_group = models.ForeignKey(RegionalGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name if self.name else "Unnamed Management Unit"
    

class ConservationUnit(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    management_unit = models.ForeignKey(ManagementUnit, on_delete=models.SET_NULL, null=True, blank=True)
    regional_group = models.ForeignKey(RegionalGroup, on_delete=models.CASCADE)
    area_in_uc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    percent_fire_affected_in_uc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.name if self.name else "Unnamed Conservation Unit"


class BurningEvent(models.Model):
    conservation_unit = models.ForeignKey(ConservationUnit, on_delete=models.CASCADE)
    wildfire_area = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    prescribed_burn_area= models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    controlled_burn_area = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    firebreak_area = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    natural_fire_area = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    isolated_indigenous_area = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    area_total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    total_prevention_area = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    total_firefighting_area = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    