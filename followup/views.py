from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

import followup
from followup import models


class CreateNew(LoginRequiredMixin, CreateView):
    """
    user record followup for organizations
    """
    login_url = 'login'
    model = models.FollowUp
    template_name = 'followup/followup_create.html'
    context_object_name = 'followup_form'
    fields = [
        'organization_name',
        'descriptions',
    ]

    def get_form(self, *args, **kwargs):
        form = super(followup.views.CreateView, self).get_form(*args, **kwargs)
        form.fields['organization_name'].queryset = models.Organization.objects.filter(creator=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.creator = self.request.user
        # self.object = form.save()
        return super().form_valid(form)


class FollowUpDetailView(LoginRequiredMixin, DetailView):
    """
    details of a followup
    """
    model = models.FollowUp
    login_url = 'login'

    def get_queryset(self):
        return models.FollowUp.objects.filter(
            creator=self.request.user
        )


class FollowUpDeleteView(LoginRequiredMixin, DeleteView):
    """
    delete a followup
    """
    model = models.Organization
    login_url = 'login'
    success_url = "/"

    def get_queryset(self):
        return models.FollowUp.objects.filter(
            creator=self.request.user
        )
