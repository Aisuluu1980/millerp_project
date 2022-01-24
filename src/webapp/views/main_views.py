from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from django.core.mail import send_mail

from webapp.forms import ContactForm
from webapp.models import Project, News, Message


class IndexView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update({
            'news_list': News.objects.order_by('-created_at')[0:4]
        })
        return context

    def get_queryset(self):
        return Project.objects.order_by('-created_date')[0:6]


class AboutView(TemplateView):
    template_name = 'about.html'

class ContactCreateView(CreateView):
    model = Message
    # fields = ["name", "phone", "email", "subject", "message"]
    success_url = reverse_lazy('webapp:success_page')
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Message from {data["name"]} {data["phone"]} Sender`s email: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)

# Функция отправки сообщения
def email(subject, content):
   send_mail(subject,
      content,
      'senedr@gmail.com',
      ['receiver@gmail.com']
   )

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
   return HttpResponse('Message sent!')