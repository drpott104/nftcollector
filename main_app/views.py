from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Nft
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'nfts/detail.html', {
        'nft': nft,
        'feeding_form': feeding_form,
    })

class NftCreate(CreateView):
    model = Nft
    fields = '__all__'

class NftUpdate(UpdateView):
    model = Nft
    fields = ['attributes']

class NftDelete(DeleteView):
    model = Nft
    success_url = '/nfts'

# def add_feeding(request, nft_id):
#     form = FeedingForm(request.POST)
#     if form.is_Valid():
#         new_feeding = form.save(commit=False)
#         new_feeding.nft_id = nft_id
#         new_feeding.save()
#     return redirect('detail', nft_id=nft_id)

def add_feeding(request, nft_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.nft_id = nft_id
        new_feeding.save()
    return redirect('detail', nft_id=nft_id)