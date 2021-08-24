from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, DeleteView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from followup import models
from organization.models import Organization


@method_decorator(csrf_exempt, name='dispatch')
class CreateNew(LoginRequiredMixin, CreateView):
    """
    user record followup for organizations
    """
    login_url = 'login'
    model = models.FollowUp
    template_name = 'followup/followup_create.html'
    fields = ('descriptions',)

    def form_invalid(self, form):
        error = form.errors
        return JsonResponse(data={
            'success': 'False',
            'error_message': 'لطفا فرم را به درستی تکمیل کنید!'
        }, status=HTTP_400_BAD_REQUEST)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.organization_name = Organization.objects.get(pk=self.kwargs['organization_pk'])
        form.save()
        return JsonResponse(data={
            'success': 'True',
            'success_message': 'پیگیری ثبت شد!'
        }, status=HTTP_201_CREATED)

    def get_context_data(self, **kwargs):
        context = {
            'organization_obj': Organization.objects.get(pk=self.kwargs['organization_pk']),
        }
        return context


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
