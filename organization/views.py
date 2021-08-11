from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import models, forms, serializers


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user organizations.
    """
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.Organization.objects.all()

    def get_queryset(self):
        user_organization = super().get_queryset()
        return user_organization.filter(creator=self.request.user)


class CreateNew(LoginRequiredMixin, CreateView):
    """
    user create new organizations
    """
    login_url = 'login'
    model = models.Organization
    form_class = forms.Organization

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class OrganizationList(LoginRequiredMixin, ListView):
    """
    list of all organizations created by a user
    """
    login_url = 'login'
    model = models.Organization
    paginate_by = 5

    def get_queryset(self):
        return models.Organization.objects.filter(
            creator=self.request.user
        )


class OrganizationEditView(LoginRequiredMixin, UpdateView):
    """
    update organization's info
    """
    model = models.Organization
    form_class = forms.Organization
    login_url = 'login'
    template_name = 'organization/organization_form.html'

    def get_queryset(self):
        return models.Organization.objects.filter(
            creator=self.request.user
        )


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    """
    delete a organization
    """
    model = models.Organization
    login_url = 'login'
    success_url = "/"

    def get_queryset(self):
        return models.Organization.objects.filter(
            creator=self.request.user
        )


class OrganizationDetailView(LoginRequiredMixin, DetailView):
    """
    details of a organization
    """
    model = models.Organization
    login_url = 'login'

    def get_queryset(self):
        return models.Organization.objects.filter(
            creator=self.request.user
        )
