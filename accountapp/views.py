from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownwership_required
from articleapp.models import Article


has_ownwership = [
    login_required,
    account_ownwership_required,
]


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "accountapp/create.html"


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = "target_user"
    template_name = "accountapp/detail.html"

    paginate_by = 25

    def get_context_data(self, **kwargs):

        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )


@method_decorator(has_ownwership, "get")
@method_decorator(has_ownwership, "post")
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = "target_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("home")
    template_name = "accountapp/update.html"


@method_decorator(has_ownwership, "get")
@method_decorator(has_ownwership, "post")
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = "target_user"
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/delete.html"
