from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MemberForm
from django.http import JsonResponse


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery')
    return render(request, 'delete_image.html', {'image': image})

def member_form(request):
    form = MemberForm()
    return render(request, "members/member_form.html", {'form': form,})

def home(request):
    members = Member.objects.all()
    return render(request, 'main.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            return render(request, "main.html", {'form': form,})
    else:
        form = MemberForm()
    return render(request, "add_member.html", {'form': form})

def main(request):
    members = Member.objects.all()
    return render(request, 'main.html')

def edit_member(request):
    mymember = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=members)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = MemberForm(instance=members)
    return render(request, 'edit_member.html')


def delete_member(request, member_id):
    mymember = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        members.delete()
        return redirect('main')
    return render(request, 'delete_member.html', {'members': members})

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mymembers' : mydata,   
  }
  return HttpResponse(template.render(context, request))