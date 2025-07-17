from rest_framework import generics, permissions
from .models import Mapping
from .serializers import MappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]


class MappingDetailView(generics.RetrieveDestroyAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatientDoctorsView(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Mapping.objects.filter(patient__id=patient_id)
