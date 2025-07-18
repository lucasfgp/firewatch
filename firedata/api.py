from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *

class BurningEventDetails(mixins.RetrieveModelMixin,
                          generics.GenericAPIView,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = BurningEvent.objects.all()
    serializer_class = BurningEventSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class BurningEventCreate(generics.CreateAPIView):
    queryset = BurningEvent.objects.all()
    serializer_class = BurningEventSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BurningEventList(generics.ListAPIView):
    queryset = BurningEvent.objects.all()
    serializer_class = BurningEventListSerializer

# Conservation Unit POST api
class ConservationUnitDetails(mixins.UpdateModelMixin,
                              generics.GenericAPIView,
                              mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin):
    queryset = ConservationUnit.objects.all()
    serializer_class = ConservationUnitSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ConservationUnitCreate(generics.CreateAPIView):
    queryset = ConservationUnit.objects.all()
    serializer_class = ConservationUnitSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ConservationUnitList(generics.ListAPIView):
    queryset = ConservationUnit.objects.all()
    serializer_class = ConservationUnitSerializer



class RegionalGroupList(generics.ListAPIView):
    queryset = RegionalGroup.objects.all()
    serializer_class = RegionalGroupSerializer



class ManagamentUnitList(generics.ListAPIView):
    queryset = ManagementUnit.objects.all()
    serializer_class = ManagementUnitSerializer

class ManagementUnitCreate(generics.CreateAPIView):
    queryset = ManagementUnit.objects.all()
    serializer_class = ManagementUnitSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
# Management Unit read, update and delete requisitions
class ManagementUnitDetails(mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin,
                            generics.GenericAPIView,
                            mixins.DestroyModelMixin):
    queryset = ManagementUnit.objects.all()
    serializer_class = ManagementUnitSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)