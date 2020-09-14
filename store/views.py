from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import ShopItem, Category, GalleryItem, DeliveryOption
from cart.forms import AddCartForm
from .forms import SendEmailForm, SearchForm
from django.core.mail import send_mail


def index_view(request):
    shop_items = ShopItem.active_items.all()
    gallery_items = GalleryItem.active_items.all()[:3]

    return render(request, 'store/index.html', {'shop_items': shop_items,'gallery_items': gallery_items})


def item_detail_view(request, slug, id):
    item = get_object_or_404(ShopItem, active=True, slug=slug, id=id)
    cart_form = AddCartForm()
    return render(request, 'store/shop-detail.html', {'item': item, 'cart_form': cart_form})


def gallery_detail_view(request, slug, id):
    gallery_item = get_object_or_404(GalleryItem, active=True, slug=slug, id=id)

    return render(request, 'store/gallery-detail.html', {'gallery_item': gallery_item})


def categories_view(request, slug=None):
    spec_category = get_object_or_404(Category, slug=slug)
    shop_items = ShopItem.active_items.filter(category=spec_category)

    return render(request, 'store/category.html', {'shop_items': shop_items, 'spec_category': spec_category})


def contact_view(request):
    form = SendEmailForm()

    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = cd['message']
            author = cd['email']

            send_mail(subject, message, author, ['happyskullpainting@gmail.com'], fail_silently=True)
            if cd['send_copy']:
                send_mail('Copy: {}'.format(subject), 'Copy of message sent in PaintingStore: \n\n{}'.format(message),
                          author, [author], fail_silently=True)
            return redirect('/thank-you/')

    else:
        form = SendEmailForm()

    return render(request, 'store/contact-us.html', {'form': form})


def about_view(request):
    return render(request, 'store/about.html')


def pricing_view(reuest):
    delivery_options = DeliveryOption.objects.all()
    return render(reuest, 'store/pricing.html', {'delivery_options': delivery_options})


def gallery_view(request):
    gallery_items = GalleryItem.active_items.all()

    return render(request, 'store/gallery.html', {'gallery_items': gallery_items})


def shop_search_form(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data['slug']
        shop_items = ShopItem.active_items.filter(name__icontains=cd)
    else:
        form = SearchForm()
        shop_items = None
    return render(request, 'store/shop.html', {'shop_items': shop_items, 'form': form})


def shop_view(request, category=None):
    if request.method == 'POST':
        return shop_search_form(request)

    else:
        shop_items = ShopItem.active_items.all()
        form = SearchForm()
        return render(request, 'store/shop.html', {'shop_items': shop_items, 'form': form})


def shop_category_view(request, slug=None):

    if request.method == 'POST':
        return shop_search_form(request)

    else:
        shop_items = ShopItem.active_items.filter(category__slug__icontains=slug)
        form = SearchForm()
        return render(request, 'store/shop.html', {'shop_items': shop_items, 'form': form})


def tahnk_you_view(request):
    return render(request, 'store/thank-you.html')


