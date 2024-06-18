from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Autos, User
from .serializers import AutosSerealizer,UserSerealizar
from .forms import AutosForm, UserForm
# Create your views here.

def get_all_autos():
    auto = Autos.objects.all().order_by('marca')
    auto_serealizer = AutosSerealizer(auto, many=True)
    return auto_serealizer.data

def get_all_user():
    user = User.objects.all().order_by('name')
    user_serealizer = UserSerealizar(user, many=True)
    return user_serealizer.data

def index_auto(request):
    auto = get_all_autos
    return render(request, 'index_auto.html', {'Autosc':auto})

def index_user(request):
    user = get_all_user
    return render(request, 'index_user.html',{'Userc':user})

def auto_rest(request):
    auto = get_all_autos()
    return JsonResponse(auto, safe=False)

def users_rest(request):
    return JsonResponse("Ok", safe=False)

# def add_auto_form(request):
#     if request.method == 'POST':
#         auto_form = AutosForm()
#         if auto_form.is_valid():
#             auto = auto_form.save()
#             return JsonResponse({'status':'sucess','result':'Ok'})
#     return JsonResponse({'status':'error'})    

class NewAutoView(CreateView):
    form_class = AutosForm
    template_name = 'form_auto.html'
    success_url = '/index_auto'

class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_user.html'
    success_url = '/index_user' 

        
