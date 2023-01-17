from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from Projeto.models import Projeto, Painel
from .models import QRcode
from .forms import QRcodeForm

# Create your views here.
def QRcodeList(request):
    qrcodeList = QRcode.objects.all()
    projectList = Projeto.objects.all()
    painelList = Painel.objects.all()
    return render(request, 'qrcode_list.html', {'qrcodelist': qrcodeList, 'projectlist': projectList, 'painellist': painelList})

def QRcodeCreate(request):
    
    form = QRcodeForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('/qrlist')
        
    return render(request, 'qrcode_form.html', {'QRcodeForm':form})

