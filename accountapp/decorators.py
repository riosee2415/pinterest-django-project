from django.contrib.auth.models import User
from django.http.response import HttpResponseForbidden


def account_ownwership_required(func):
    def decorated(request, *args, **kwargs):

        user = User.objects.get(pk=kwargs["pk"])

        if not user == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated
