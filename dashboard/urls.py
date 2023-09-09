from django.urls import path

from dashboard.views import PolicyListCreateView, PolicyDetailView, FilteredPolicyListView

urlpatterns = [
    path('policies', PolicyListCreateView.as_view(), name='policy-list-create'),
    path('policies/filter/', FilteredPolicyListView.as_view(), name='filtered-policy-list'),
    path('policies/<int:pk>', PolicyDetailView.as_view(), name='policy-detail'),
]
