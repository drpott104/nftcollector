from django.shortcuts import render
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Nft

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def nfts_index(request):
    nfts = Nft.objects.all()
    return render(request, 'nfts/index.html', { 'nfts': nfts })

def nfts_detail(request, nft_id):
    nft = Nft.objects.get(id=nft_id)
    return render(request, 'nfts/detail.html', { 'nft': nft })
