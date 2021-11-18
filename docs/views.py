from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


from .forms import *
from .models import *


class StudenSearch(ListView):
    model = Students
    template_name = 'docs/index.html'
    context_object_name = 'posts'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Students.objects.filter(name__icontains=query)
        return object_list


class StudentHome(ListView):
    model = Students
    template_name = 'docs/index.html'
    context_object_name = 'posts'


def about(request):
    return render(request, 'docs/about.html')


class AddObhodnoi(CreateView):
    form_class = AddObhodnoiForm
    template_name = 'docs/addpage.html'
    success_url = reverse_lazy('home')



def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowStudent(DetailView):
    model = Students
    template_name = 'docs/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


# NEW Experiment
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    'student': Obhodnoi.student,
    'email': Obhodnoi.email,
}


# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('docs/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('app/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def index(request):
    context = {}
    return render(request, 'app/index.html', context)

