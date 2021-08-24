from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView, FormView, DeleteView
from django.views.generic.detail import SingleObjectMixin

import organization
from quote import models, forms, tasks


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'quote/main.html'


class QuoteListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = models.Quote
    paginate_by = 5
    template_name = 'quote/quote_list.html'

    def get_queryset(self):
        return models.Quote.objects.filter(
            creator=self.request.user
        )


class QuoteCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.Quote
    template_name = 'quote/quote_create.html'
    fields = [
        'organization_name',
    ]

    def get_form(self, *args, **kwargs):
        form = super(organization.views.CreateView, self).get_form(*args, **kwargs)
        form.fields['organization_name'].queryset = models.Organization.objects.filter(creator=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'پیش فاکتور اضافه شد.'
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('quote:quote-edit', kwargs={'pk': self.object.pk})


class QuoteDetailView(LoginRequiredMixin, DetailView):
    model = models.Quote
    template_name = 'quote/quote_detail.html'

    def get_queryset(self):
        return models.Quote.objects.filter(
            creator=self.request.user
        )


class QuoteEditView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = models.Quote
    template_name = 'quote/quote_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Quote.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Quote.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return forms.QuoteItemFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'تغییرات ذخیره شد.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('quote:quote-detail', kwargs={'pk': self.object.pk})


class QuoteDeleteView(DeleteView):
    """
    delete a quote
    """
    model = models.Quote
    success_url = reverse_lazy('quote:quote-list')

    def get_queryset(self):
        return models.Quote.objects.filter(
            creator=self.request.user
        )


@login_required
def send_email_quote(request, pk):
    quote = models.Quote.objects.get(pk=pk, creator=request.user)
    content = render_to_string('quote/quote_detail.html', {'object': quote})
    sender = request.user.username
    receiver = quote.organization_name.email
    if quote:
        tasks.email_quote_task.delay(content, sender, receiver)
        messages.success(request, 'ایمیل ارسال شد')
    return redirect('/quote/quote-list/')
