from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from . import models, forms


class CreateNew(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.Organization
    form_class = forms.Organization

    # success_url = 'home'

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
    template_name = 'organization/organization_form.html'

    # success_url = ''

    def get_queryset(self):
        return models.Organization.objects.filter(
            creator=self.request.user
        )


class OrganizationDeleteView(DeleteView):
    """
    delete a organization
    """
    model = models.Organization
    success_url = "/"

    def get_queryset(self):
        return models.Organization.objects.filter(
            creator=self.request.user
        )


class OrganizationDetailView(DetailView):
    """
    details of a organization
    """
    model = models.Organization

    def get_queryset(self):
        return models.Organization.objects.filter(
            creator=self.request.user
        )
