from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class checkLogin(MiddlewareMixin):

    def process_request(self, request):

        # if not login page
        if request.path != "/auth/login/":

            # if no auth user
            if not request.user.is_authenticated:

                return redirect('auth:login')
        else:
            # if login page

            if request.user.is_authenticated:
                return redirect('dashboard:home')
