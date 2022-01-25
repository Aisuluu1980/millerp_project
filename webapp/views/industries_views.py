from django.shortcuts import render
from django.views.generic import TemplateView

class FinanceView(TemplateView):
    template_name = 'industries/finance.html'

class ProcurementView(TemplateView):
    template_name = 'industries/procurement.html'

class SafetytView(TemplateView):
    template_name = 'industries/safety.html'

class HumanResoursesView(TemplateView):
    template_name = 'industries/hr.html'

class CustomerView(TemplateView):
    template_name = 'industries/customer.html'

class MobileView(TemplateView):
    template_name = 'industries/mobile.html'

class DocumentView(TemplateView):
    template_name = 'industries/document.html'

class MigrationView(TemplateView):
    template_name = 'industries/migration.html'


class AssetView(TemplateView):
    template_name = 'industries/asset.html'


# def finance(request):
#     data = {"header": "Hello Django", "message": "Welcome to Python"}
#     return render(request, "industries/finance.html", context=data)

