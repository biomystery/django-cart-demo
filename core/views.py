from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import (View, TemplateView, DetailView, ListView,
                                    CreateView, UpdateView, DeleteView)

from core.models import Product, OrderItem, Order, UserProfile, Category, UserProfile
from core.forms import UserForm, UserProfileForm
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
#Product views
class ProductDetailView(DetailView):
    context_object_name = 'product_detail'
    model = Product
    template_name = "core/product_detail.html"
class ProductListView(ListView):
    context_object_name = 'products'
    model = Product
    template_name = "core/product_list.html"
class ProductCreateView(CreateView):
    fields = ('name', 'price_ht', 'category')
    model = Product

class ProductUpdateView(UpdateView):
    fields = ('name', 'price_ht')
    model = Product
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("core:list")
# Product Categories views
class CategoryDetailView(DetailView):
    context_object_name = 'category_detail'
    model = Category
    template_name = "core/category_detail.html"
class CategoryListView(ListView):
    context_object_name = 'categories'
    model = Category
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
    model = Category
class CategoryUpdateView(UpdateView):
    fields = ('name', 'description')
    model = Category
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("core:category_list")
# UserProfile views
class UserProfileDetailView(DetailView):
    context_object_name = 'userprofile_detail'
    model = UserProfile
    template_name = "core/userprofile_detail.html"

class UserProfileListView(ListView):
    context_object_name = 'profiles'
    model = UserProfile
    template_name = "core/userprofile_list.html"

class UserProfileCreateView(CreateView):
    fields = ('user', 'portfolio_site')
    model = UserProfile

class UserProfileUpdateView(UpdateView):
    fields = ('user', 'portfolio_site')
    model = UserProfile


class UserProfileDeleteView(DeleteView):
    model = UserProfile
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid login details entered!")
    else:
        return render(request, 'core/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def get_user_pending_order(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0
@login_required
def add_to_cart(request, pk):
    cart_profile = get_object_or_404(UserProfile, user=request.user)
    cart_product = get_object_or_404(Product, pk=pk)
    cart_item,created = OrderItem.objects.get_or_create(product=cart_product)
    cart_order,created = Order.objects.get_or_create(owner=user, is_ordered=False)
    amount = OrderItem.objects.get_or_create(quantity = quantity)
    cart_order.items.add(cart_item)
    cart_order.quantity += 1
    cart_order.save()
    messages.info(request, "item has been added")
    return redirect(reverse_lazy("core:list"))
@login_required
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'core/order_summary.html', context)
