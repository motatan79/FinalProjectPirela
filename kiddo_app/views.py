from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from .models import RegisteredUser, Pais, Tienda, Evento
from django.core.exceptions import ObjectDoesNotExist 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

def index(request):
    return render(request, "index.html")

def app_homepage(request):
    try:
        if usrnme:
            userdetails = {'username': usrnme}
            return render(request, "loggedin.html", userdetails)
    except NameError:
        return render(request, 'index.html')

        #return render(request, 'homepage.html')

def about_us(request):
    try:
        if usrnme:
            return render(request, 'aboutUs.html')
    except NameError:
        return render(request, 'aboutUs.html')


def services(request):
    try:
        if usrnme:
           return render(request, 'services.html')
    except NameError:
        return render(request, 'services.html')


def contact_us(request):
    try:
        if usrnme:
           return render(request, 'contactUs.html')
    except NameError:
        return render(request, 'contactUs.html')
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def registrar_cliente(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitósamente")
            return redirect("registrados")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "registercliente.html", user_info)
    
# def signin(request):
#     return render(request, 'signin.html')


# Creación de la vista sign-in
# def signin(request):
#     global usrnme
#     if request.method == 'POST':
#         usrnme = request.POST['username']
#         psswrd = request.POST['pswd']
        
#         try:
#             user = RegisteredUser.objects.get(name=usrnme)
#             if usrnme == user.name and psswrd == user.password:
#                 return redirect('loggedin')
#             else:
#                 messages.info(request, "Clave incorrecta")
#                 return redirect("signin")
#         except ObjectDoesNotExist:
#             messages.info(request, "El usuario no existe")
#             return redirect("signin")
#     else:
#         return render(request, "signin.html")
    
    
def loggedin(request):
    userdetails = {'username': usrnme}
    return render(request, "loggedin.html", userdetails)

def logout(request):
    global usrnme
    del usrnme
    return render(request, "logout.html")


def pais(request):
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "País creado exitósamente")
            return redirect("paisesregistrados")
    else:
        form = PaisForm()
        user_info = {'form': form}
        return render(request, "registerpais.html", user_info)
    
    
def tienda(request):
    if request.method == "POST":
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tienda creada exitósamente")
            return redirect("tiendasregistradas")
    else:
        form = TiendaForm()
        user_info = {'form': form}
        return render(request, "registertienda.html", user_info)

def evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento creado exitósamente")
            return redirect("eventosagendados")
    else:
        form = EventoForm()
        user_info = {'form': form}
        return render(request, "registerevento.html", user_info)
    
    
def registrados(request):
    clientes = RegisteredUser.objects.all()
    return render(request, "registrados.html", {"clientes": clientes})

def eventosagendados(request):
    eventos_agendados = Evento.objects.all()
    return render(request, "eventosagendados.html", {"eventos_agendados": eventos_agendados})

def tiendas_registradas(request):
    tiendas = Tienda.objects.all()
    return render(request, "tiendas_registradas.html", {"tiendas": tiendas})

def paises_registrados(request):
    paises = Pais.objects.all()
    return render(request, "paises_registrados.html", {"paises": paises})

def buscar_tienda(request):
    nombre_tienda = None
    descripcion = None
    ciudad = None
    existe_tienda = False
    
    if request.method == 'POST':
        # Obtener el nombre de la tienda desde la solicitud POST
        nombre_tienda = request.POST.get('nombre_tienda', None)
        
        if nombre_tienda:
            tienda = Tienda.objects.filter(nombre=nombre_tienda).first()
                    
            if tienda is not None:
                descripcion = tienda.descripcion
                ciudad = tienda.ciudad
                existe_tienda = True
        
            # Retornar el resultado en una respuesta HTTP
            return render(request, 'buscar_tienda.html', {'nombre_tienda': nombre_tienda,
                                                          'descripcion' : descripcion,
                                                          'ciudad': ciudad,
                                                          'existe_tienda': existe_tienda})
            

    # Manejar el caso en el que no se proporciona el nombre o el método no es POST
    return render(request, 'buscar_tienda.html', {'nombre_tienda': None, 'existe_tienda': False})


# Buscar información haciendo uso de las clases de Django
class UserListView(ListView):
    model = RegisteredUser
    template_name = 'user_data.html'
    context_object_name = 'alldata'
    
class UserDetailView(DetailView):
    model = RegisteredUser
    
class UserCreateView(CreateView):
    model = RegisteredUser
    form_class = RegisterForm
    success_url = reverse_lazy("registrados")
    #fields = '__all__'
    
# Para que solo los administradores puedan modificar los datos se usa la clase UserPassesTestMixin    
class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = RegisteredUser
    form_class = RegisterForm
    
    def test_func(self) -> bool:
        return self.request.user.is_authenticated and self.request.user.is_superuser
        # if self.request.user.is_active:
        #     return True
        # else:
        #     return False
    def handle_no_permission(self) -> HttpResponseRedirect:
        return HttpResponseRedirect(reverse_lazy('registrados'))

# Para que solo los administradores puedan borrar los datos se usa la clase UserPassesTestMixin    
class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = RegisteredUser
    success_url = reverse_lazy('registrados')
    
    def test_func(self) -> bool:
        if self.request.user.is_active:
            print(self.request.user)
            return True
        else:
            return False
        
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "signin.html"