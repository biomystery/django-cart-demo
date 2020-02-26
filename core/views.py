from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, DetailView, ListView,
                                    CreateView, UpdateView, DeleteView)
from .  import models
from core.forms import UserForm, UserProfileForm
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
#Product views
class ProductDetailView(DetailView):
    context_object_name = 'product_detail'
    model = models.Product
    template_name = "core/product_detail.html"
class ProductListView(ListView):
    context_object_name = 'products'
    model = models.Product
    template_name = "core/product_list.html"
class ProductCreateView(CreateView):
    fields = ('name', 'price_ht', 'category')
    model = models.Product

class ProductUpdateView(UpdateView):
    fields = ('name', 'price_ht')
    model = models.Product
class ProductDeleteView(DeleteView):
    model = models.Product
    success_url = reverse_lazy("core:list")
# Product Categories views
class CategoryDetailView(DetailView):
    context_object_name = 'category_detail'
    model = models.Category
    template_name = "core/category_detail.html"
class CategoryListView(ListView):
    context_object_name = 'categories'
    model = models.Category
    def get_products(request):
         products = category.products.all()
         context = {
           'title': category.name,
           'products': products,
         }
         return render(request,'core/category_list.html',context)
    template_name = "core/category_list.html"
class CategoryCreateView(CreateView):
    fields = ('name', 'description')
    model = models.Category
class CategoryUpdateView(UpdateView):
    fields = ('name', 'description')
    model = models.Category
class CategoryDeleteView(DeleteView):
    model = models.Category
    success_url = reverse_lazy("core:category_list")
# UserProfile views
class UserProfileDetailView(DetailView):
    context_object_name = 'userprofile_detail'
    model = models.UserProfile
    template_name = "core/userprofile_detail.html"

class UserProfileListView(ListView):
    context_object_name = 'profiles'
    model = models.UserProfile
    template_name = "core/userprofile_list.html"

class UserProfileCreateView(CreateView):
    fields = ('user', 'portfolio_site')
    model = models.UserProfile

class UserProfileUpdateView(UpdateView):
    fields = ('user', 'portfolio_site')
    model = models.UserProfile


class UserProfileDeleteView(DeleteView):
    model = models.UserProfile
    success_url = reverse_lazy("core:profile_list")
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            #encoding the user's pw
            user.set_password(user.password)
            #save the envryption
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'core/register.html',
                            {'user_form':user_form,
                                'profile_form':profile_form,
                                'registered':registered})
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item,created = OrderItem.objects.get_or_create(product = product)
    cart_order,created = Order.objects.get_or_create(owner=user, is_ordered=False)
    cart_order.items.add(cart_item)
    cart_order.quantity += 1
    cart_order.save()
    messages.info(request, "item has been added")
    return redirect(reverse_lazy("core:list"))

def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'core/order_summary.html', context)
