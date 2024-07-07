from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_function(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')

        return view_func(self, request, *args, **kwargs)

    return wrapper_function
