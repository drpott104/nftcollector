from django.shortcuts import render
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Nft

nfts = [
    {'name': '#9900', 'collection': 'Toxic Skulls Club', 'attributes': 'fumes, diamonds, trickster', 'date': 'Jan 18, 2023'},
    {'name': '#7686', 'collection': 'Toxic Skulls Club', 'attributes': 'fumes, spikes, sailor', 'date': 'Nov 23, 2022'},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def nfts_index(request):
    return render(request, 'nfts/index.html', {
        'nfts': nfts
    })
