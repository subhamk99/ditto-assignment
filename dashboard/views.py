from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, filters, status
from django_filters import rest_framework as django_filters

from .filters import PolicyDateFilter
from .models import Policy
from .serializers import PolicySerializer


class PolicyListCreateView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    filter_backends = (filters.OrderingFilter, django_filters.DjangoFilterBackend)
    filter_set_fields = ('policy_status', 'customer_name')
    ordering_fields = '__all__'
    filter_class = PolicyDateFilter


class FilteredPolicyListView(PolicyListCreateView):
    def get_queryset(self):
        queryset = super().get_queryset()

        # Apply filters based on query parameters
        policy_status = self.request.query_params.get('policy_status')
        customer_name = self.request.query_params.get('customer_name')

        if policy_status:
            queryset = queryset.filter(policy_status=policy_status)

        if customer_name:
            queryset = queryset.filter(customer_name=customer_name)

        return queryset


class PolicyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
