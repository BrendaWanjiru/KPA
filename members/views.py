from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import ImageForm, MemberForm
from .models import Image
from .models import Member

# views.py
# views.py
def about_us_view(request):
    members = [
        {
            'photo': '',
            'name': 'John Doe',
            'position': 'Developer',
            'bio': 'John is a full-stack developer with 5 years of experience.'
        },
        {
            'photo': 'static/images/IMG_6473.jpeg',
            'name': 'Jane Smith',
            'position': 'Designer',
            'bio': 'Jane is a creative designer who specializes in UI/UX.'
        },
        # Add more members as needed
    ]
    print(members)  # Debugging line
    return render(request, 'about_us.html', {'members': members})




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

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = MemberForm()
    return render(request, "add_member.html", {'form': form})

def edit_member(request, id):
    mymember = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=mymember)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = MemberForm(instance=mymember)
    return render(request, 'edit_member.html', {'form': form})

def delete_member(request, member_id):
    mymember = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        mymember.delete()
        return redirect('main')
    return render(request, 'delete_member.html', {'member': mymember})

def members(request):
    mymembers = Member.objects.all().values()
    return render(request, 'all_members.html', {'mymembers': mymembers})

def details(request, id):
    mymember = get_object_or_404(Member, id=id)
    return render(request, 'details.html', {'mymember': mymember})

def main(request):
    members = Member.objects.all()
    return render(request, 'main.html', {'members': members})

def testing(request):
    mymembers = Member.objects.all()
    return render(request, 'template.html', {'mymembers': mymembers})

def events(request):
    members = Member.objects.all()
    return render(request, 'events.html', {'members': members})

def about_us(request):
    members = Member.objects.all()
    return render(request, 'about_us.html', {'members': members})