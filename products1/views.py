from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import dummproduts,Productinshop,Product
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    tdummproduts = Productinshop.objects.all()
    return render(request,'index.html',{'products':tdummproduts})

def render_to_pdf(template_src,context_dict={}):

    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("iso-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return
data = {
    "products": Productinshop.objects.all(),

        }
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        tdummproduts = Productinshop.objects.all()
        pdf = render_to_pdf('dummy.html',data)
        return HttpResponse(pdf,content_type="application/pdf")
def ProductId(request):
    productsID = Product.objects.all()
    val1 = request.POST["prId"]
    return render(request,'PRODUCT.html',{'result':val1,'products':productsID})
@csrf_exempt
def nsdlesign(request):
    val1 = request.POST["msg"]
    return render(request, 'nsdlesign.html', {'result': val1})
