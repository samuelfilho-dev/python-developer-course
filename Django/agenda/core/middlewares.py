from django.http import Http404


class PermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not user_has_permission(request.user):
            raise Http404

        response = self.get_response(request)
        return response


def user_has_permission(user):
    return True
