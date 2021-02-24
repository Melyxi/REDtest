from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect,  reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from authapp.forms import EditFormUser, EditFormAdmin, EditFormDev
from authapp.models import User


def main(request):
    return render(request, 'mainapp/index.html')


#@user_passes_test(lambda u: u.is_superuser)
def dev(request):
    if not request.user.is_anonymous:
        if request.user.is_superuser:
            users = User.objects.filter(role='USER')
            administrators = User.objects.filter(role='ADMIN')
            developers = User.objects.filter(is_superuser=True)

            content = {'users': users, 'administrators': administrators, 'developers': developers}

            return render(request, 'mainapp/developer.html', content)
        else:
            return HttpResponseNotFound('<h1> Page not found</h1>')
    else:
        return HttpResponseNotFound('<h1> Page not found</h1>')



#@user_passes_test(lambda u: u.is_superuser or u.role == 'ADMIN' if not u.is_anonymous else False)
def admin(request):
    if not request.user.is_anonymous:
        if request.user.role == 'ADMIN' or request.user.is_superuser:
            print(request.user.role, 'admin')
            users = User.objects.filter(role='USER')
            administrators = User.objects.filter(role='ADMIN')

            content = {'users': users, 'administrators': administrators}

            return render(request, 'mainapp/administrator.html', content)
        else:
            return HttpResponseNotFound('<h1> Page not found</h1>')
    else:
        return HttpResponseNotFound('<h1> Page not found</h1>')


#@user_passes_test(lambda u: u.is_superuser or (u.role == 'ADMIN' if not u.is_anonymous else False) or (
#u.role == 'USER' if not u.is_anonymous else False))

def user(request):
    if not request.user.is_anonymous:
        if request.user.role == 'ADMIN' or request.user.role == 'USER' or request.user.is_superuser:
            print(request.user.role, 'user')
            username = request.user.username

            user = User.objects.filter(username=username).first

            content = {'user': user}

            return render(request, 'mainapp/user.html', content)
        else:
            return HttpResponseNotFound('<h1> Page not found</h1>')
    else:
        return HttpResponseNotFound('<h1> Page not found</h1>')




class AdminUpdateView(UpdateView):
    model = User
    template_name = 'authapp/edit.html'
    success_url = reverse_lazy('main:admin')
    # fields = '__all__'
    form_class = EditFormAdmin


    @method_decorator(user_passes_test(lambda u: u.is_superuser or u.role == 'ADMIN'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(is_superuser=True)



class DevUpdateView(UpdateView):
    model = User
    template_name = 'authapp/edit.html'
    success_url = reverse_lazy('main:dev')
    # fields = '__all__'
    form_class = EditFormDev


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

