from django.shortcuts import render, redirect

from forum.forms.register import RegisterForm
from forum.forms.user import UserCreationForm
from forum.models.forum import Forum
from django.views.generic.list import ListView
from django.views import View


class ForumListView(ListView):
    model = Forum
    context_object_name = "forums"
    template_name = 'forum_list.htm'


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


class RegisterView(View):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})
