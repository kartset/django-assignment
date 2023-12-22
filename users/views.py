from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader
from .models import Users
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from .form import UserForm


# Create your views here.

def index(req):
    print(req)
    if req.GET.get('test_id') :
        return getOne(req, req.GET.get('test_id'))
    else :
        users = Users.objects.all()
        template = loader.get_template("users/list.html")
        context = {
            "users": users,
        }
        return HttpResponse(template.render(context, req))

def getOne(req, test_id):
    user = get_object_or_404(Users, test_id=test_id)
    template = loader.get_template("users/detail.html")
    context = {
        "user": user,
    }
    return HttpResponse(template.render(context, req))
    

def getOneJSON(req):
    test_id = req.GET.get('test_id')
    all_entries = Users.objects.filter(test_id=test_id)
    entries_list = [
        {field.name: getattr(entry, field.name) for field in entry._meta.fields}
        for entry in all_entries
    ]
    return JsonResponse({'users': entries_list}, safe=False)
    

def create(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        print('form', req.POST)
        if form.is_valid():
            new_post = form.save()
            return JsonResponse({'status': 'success', 'message': 'Post created successfully', 'id': new_post.id})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})
