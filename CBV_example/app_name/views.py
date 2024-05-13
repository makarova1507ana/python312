from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class Index(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass

class PageTemplate(TemplateView):
    template_name = 'page_Template_View.html'
    extra_context = {
         'name': 'Template_View страница',
         #'menu': menu,
         #'posts': Post.objects.all() #Women.published.all().select_related('cat'),
    }

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs) # context - словарь
         # m = model.objects.all()[:5]
         # context['key'] = m
         #context['title'] = 'Главная страница'
         # context['menu'] = menu
         # context['posts'] = Women.published.all().select_related('cat')
         context['id'] = int(self.request.GET.get('id'))
         return context