
from django.shortcuts import render,HttpResponseRedirect, redirect
from django.views.generic import CreateView
from django.db import transaction
import json

from .models import Qurilish
from .forms import CollectionTitleForm, CollectionTitleFormSet


class Qurilish_view(CreateView):
    model = Qurilish
    template_name = 'app/test.html'
    form_class = CollectionTitleForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(Qurilish_view, self).get_context_data()
        if self.request.POST:
            data['q_type'] = CollectionTitleFormSet(self.request.POST)
        else:
            data['q_type'] = CollectionTitleFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        q_type = context['q_type']
        with transaction.atomic():
            form.instance.author = self.request.user
            self.object = form.save()
            if q_type.is_valid():
                q_type.instance = self.object
                q_type.save()
        return super(Qurilish_view, self).form_valid(form)
    














#
# def sendjson(request):
#
#     if request.method == "POST":
#         data = QurilishForm(request.POST)
#         data1 = json.loads(request.POST.get('data'))
#         print(data)
#         if data.is_valid():
#             data.save(commit=False)
#             return redirect('/')
#         else:
#             data = QurilishForm()
#             return render(request, 'app/test.html', {'data':data})
