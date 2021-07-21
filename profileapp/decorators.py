from profileapp.models import Profile
from django.http.response import HttpResponseForbidden


def profile_ownwership_required(func):
    def decorated(request, *args, **kwargs):

        profile = Profile.objects.get(pk=kwargs["pk"])

        if not profile.user == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated
