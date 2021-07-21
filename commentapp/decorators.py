from commentapp.models import Comment
from django.http.response import HttpResponseForbidden


def comment_ownwership_required(func):
    def decorated(request, *args, **kwargs):

        comment = Comment.objects.get(pk=kwargs["pk"])

        if not comment.writer == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated
