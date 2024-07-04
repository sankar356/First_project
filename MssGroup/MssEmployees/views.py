from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .form import UserForm, RolesForm, User_details_forms, DataForm
from .models import Employees, UserData
from .serializer import EmployeesSerializers


# Create your views here.
@api_view(['Post', 'Get'])
def index(request):
    name = EmployeesSerializers(data=request.data)
    if request.method == 'Post':
        if name.is_valid():
            name.save()
            return Response(name.data, status=status.HTTP_201_CREATED)

        else:
            return Response(name.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        name = Employees.objects.all()
        serializer = EmployeesSerializers(name, many=True)
        return Response(serializer.data)


def newAdmin(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data uploded")
        else:
            return HttpResponse("sorry bro")
    form = UserForm()
    return render(request, r"MssEmp\\register.html", context={"form": form})


def user(request):
    if request.method == "POST":
        form = RolesForm(request.POST)
        if form.is_valid():
            form.save()
            return
        else:
            return HttpResponse("sorry bro")
    form = RolesForm()
    return render(request, r"MssEmp\\user.html", context={"form": form})


def master(request):
    if request.method == "POST":
        form = User_details_forms(request.POST)
        if form.is_valid():
            form.save()
            return
        else:
            return HttpResponse("sorry bro")
    form = User_details_forms()
    return render(request, r"MssEmp\\user.html", context={"form": form})


def user_register(request):
    return render(request, r'MssEmp\\register.html')


def Register(request):
    if request.method == 'POST':
        print(request)
        if (request.POST.get('user_name'), request.POST.get('email'), request.POST.get('password') ):
            register = UserData()
            register.user_name = request.POST.get('user_name')
            register.email = request.POST.get('email')
            register.password = request.POST.get('password')
            register.save()
            return HttpResponse('done huu')
        else:
            return HttpResponse('not connect')

    form = DataForm()
    return render(request, r'MssEmp\\register.html', {"form": form})


# def Register(request):
#     if request.method == 'post':
#         user_name = request.POST.get('user_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         userData = UserData(user_name=user_name, email=email, password=password)
#         userData.save()
#
#         return HttpResponse("data uploded")
#     else:
#         return HttpResponse("sorry bro")

# def dashboard(request):
#     if request.method == "POST":
#         form = DweetForm(request.POST)
#         if form.is_valid():
#             dweet = form.save(commit=False)
#             dweet.user = request.user
#             dweet.save()
#     form = DweetForm()
#     return render(request, "dwitter/dashboard.html", {"form": form})

# if request.method == 'POST':
#     patient_name = request.POST.get('patient_name')
#     blood_group = request.POST.get('blood_group')
#
#     # Create a new patient entry in the database using the Patient model
#     patient = Patient(patient_name=patient_name, blood_group=blood_group)
#     patient.save()
#
#     return HttpResponse("Data successfully inserted!")
# else:
#     return HttpResponse("Invalid request method.")
# def update(request, id):
#   mymember = Member.objects.get(id=id)
#   template = loader.get_template('update.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))
# def Register(request, id):
#     data = UserData.object.get(id=id)
#     template = loader.get_template('MssEmp\\register.html')
#     context = {
#         "data": data
#     }
#     return HttpResponse(template.render(context, request))


# def my_api_view(request):
#     if request.method == 'GET':
#         # Handle GET request
#         data = {'message': 'This is a GET request'}
#         return Response(data)
#     elif request.method == 'POST':
#         # Handle POST request
#         data = {'message': 'This is a POST request'}
#         return Response(data)
# def index(request):
#     return (
#
#     )
# return render(request,"D:\project_two\MssGroup\MssEmployees\Template\mssEmployee\index.html")

# def Register(request):
#     if request.method == "POST":
#         data = UserDataForm(request.POST)
#         if data.is_valid():
#             data.save()
#             return HttpResponse("data uploded")
#         else:
#             return HttpResponse("sorry bro")
#
#     data = UserData()
#     return render(request, r"MssEmp\\register.html", context={"data": data})
