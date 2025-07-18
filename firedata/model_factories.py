import factory

from .models import *

# model_factories.py

class RegionalGroupFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Grupo Regional {n}")

    class Meta:
        model = RegionalGroup

class ManagementUnitFactory(factory.django.DjangoModelFactory):
    name = "Núcleo de Gestão Integrada - ICMBio Recife"
    regional_group = factory.SubFactory(RegionalGroupFactory)

    class Meta:
        model = ManagementUnit

class ConservationUnitFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"UC Test {n}")
    management_unit = factory.SubFactory(ManagementUnitFactory)
    regional_group = factory.SubFactory(RegionalGroupFactory)
    area_in_uc = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    percent_fire_affected_in_uc = factory.Faker('pydecimal', left_digits=1, right_digits=2, positive=True)

    class Meta:
        model = ConservationUnit


class BurningEventFactory(factory.django.DjangoModelFactory):
    conservation_unit = factory.SubFactory(ConservationUnitFactory)
    wildfire_area = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    prescribed_burn_area = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    controlled_burn_area = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    firebreak_area = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    natural_fire_area = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    isolated_indigenous_area = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    area_total = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    total_prevention_area = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    total_firefighting_area = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)

    class Meta:
        model = BurningEvent