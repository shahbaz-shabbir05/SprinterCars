from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View

from sprintercars import settings
from sprintercarsapp.forms import ContactForm
from sprintercarsapp.models import Products, SliderImages, Testimonial


class BaseView(generic.TemplateView):
    template_name = 'base.html'


class IndexView(generic.TemplateView):
    model = Products, SliderImages, Testimonial
    template_name = 'index.html'
    context_object_name = 'latest_products'

    def get(self, request, *args, **kwargs):
        latest_products = Products.objects.filter(is_latest=True)
        slider_images = SliderImages.objects.all()
        testimonials = Testimonial.objects.all()
        return render(request, self.template_name, {'latest_products': latest_products,
                                                    'slider_images': slider_images, 'testimonials': testimonials})


class ContactView(generic.TemplateView):
    template_name = 'contact_us.html'


class AboutView(generic.TemplateView):
    model = Products
    template_name = 'about.html'
    context_object_name = 'sold_products'

    def get(self, request, *args, **kwargs):
        sold_products = Products.objects.filter(is_sold=True)
        all_products = Products.objects.all()
        return render(request, self.template_name, {'sold_products': sold_products, 'all_products': all_products})


class PartnersView(generic.TemplateView):
    template_name = 'partners.html'


class DetailView(generic.TemplateView):
    model = Products
    template_name = 'detail.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        pid = kwargs.get("pid")
        products = Products.objects.filter(id=pid).first()
        return render(request, self.template_name, {'products': products})


class ProductsView(generic.ListView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        products = Products.objects.all()
        return render(request, self.template_name, {'products': products})

    def post(self, request):
        request_data = request.POST.copy()
        pid = request_data.get('pid')
        name = request.POST.get('pname')
        image = request_data.get('pimage')
        subject = "Interested Products"
        message = "Product ID: " + pid + "\n" + "Product Name: " + name + "\n" + "Product Image: " + image + "\n"
        html_message = '<img src="cid:{{ image }}">'
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER],
                      fail_silently=False, html_message=html_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('products')


def search(request):
    if request.method == 'GET':
        product_name = request.GET.get('s')
        products = Products.objects.filter(name__icontains=product_name)
        return render(request, "search.html", {"products": products, "search_keyword": product_name})
    else:
        return render(request, "search.html", {})


class ContactFormView(View):
    form_class = ContactForm
    template_name = 'contact_us.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            subject = "Email From Contact Form"
            from_email = form.cleaned_data['from_email']
            msg = form.cleaned_data['message']
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            phone_number = form.cleaned_data['phone']
            message = "Name: " + first_name + " " + second_name + "\n" + "Phone Number: " + phone_number + "\n" + \
                      "Email: " + from_email + "\n" + "Message: " + msg
            html_message = '<h1>This is my HTML test</h1>'
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER],
                          fail_silently=False, )  # html_message=html_message )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
        return render(request, self.template_name, {'form': form})

