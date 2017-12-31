####django imports ####
from django.shortcuts import render
from django.views import View

#### our app imports ####

#### others ####.

class Home(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

