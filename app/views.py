from django.shortcuts import render
from app.forms import MyUserForm
from app.models import MyUser
from django.http import JsonResponse
from django.http import HttpResponse
import json


def home(request):
    form = MyUserForm()
    stud = MyUser.objects.all()
    return render(request, 'app/index.html', {'form':form, 'stu':stud})


def add_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        a = data.get('id')
        
        if not a == '':
            usr = MyUser(id=a, name=data['name'], email=data['email'], password=data['password'])
            usr.save()
        else:
            form = MyUserForm(data)
            if form.is_valid():
                form.save()
            else:
                return JsonResponse({'status': '0'})
            
        updatedStu = list(MyUser.objects.values())
        return JsonResponse({'status': 'Saved', 'updatedStu':updatedStu})
            
    return HttpResponse("Add_data")


def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data['sid']
        model_data = MyUser.objects.get(id=id)
        model_data.delete()
        updatedStu = list(MyUser.objects.values())
        return JsonResponse({'status':'deleted', 'updatedStu':updatedStu})
    else:
        return JsonResponse({'status': '0'})
    

def edit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data['sid']
        md = MyUser.objects.get(id=id)
        updatedStu = {'id':md.id, 'name':md.name, 'email':md.email, 'password':md.password}
        return JsonResponse({'status':'edited', 'updatedStu':updatedStu})
    else:
        return JsonResponse({'status': '0'})




