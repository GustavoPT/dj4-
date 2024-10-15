# from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate,login 
# from ..djangoecommerce4.models import Product
# from django.core.paginator import Paginator
# from django.views.generic import ListView 
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from ..djangoecommerce4.models import Rating

# class ProductListView(ListView):
#     queryset = Product.objects.all()
#     template_name = "products/list.html"

# def products(request):
#     product_objects = Product.objects.all()
#     print(product_objects[0].title)
#     print(product_objects[0].price)
    
#     item_name = request.GET.get('item_name')

#     if item_name != '' and item_name is not None:
#         print("here")
#         product_objects = product_objects.filter(title__icontains=item_name)

#     paginator = Paginator(product_objects, 4)
   
#     page = request.GET.get('page')

#     product_objects = paginator.get_page(page)
#     return render(request,'shop/index.html',{'product_objects':product_objects})

# def rating(request):
#     obj = Rating.objects.get
#     context = {}
#     return render(request,'rating.html',{})

# def login(request):
#     return render(request,"authentication/authentication.html")

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username,password=password)
#             login(request,user)
#             return redirect('index')
#     else:
#         form = form = UserCreationForm()
#     context = {'form' : form}
#     return render(request,'registration/register.html',context)