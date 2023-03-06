from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Nft, Pet
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
    id_list = nft.pets.all().values_list('id')
    pets_nft_doesnt_have = Pet.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'nfts/detail.html', {
        'nft': nft, 'feeding_form': feeding_form,
        'pets': pets_nft_doesnt_have
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

class PetList(ListView):
  model = Pet

class PetDetail(DetailView):
  model = Pet

class PetCreate(CreateView):
  model = Pet
  fields = '__all__'

class PetUpdate(UpdateView):
  model = Pet
  fields = ['name', 'description']

class PetDelete(DeleteView):
  model = Pet
  success_url = '/pets'

def assoc_pet(request, nft_id, pet_id):
  Nft.objects.get(id=nft_id).pets.add(pet_id)
  return redirect('detail', nft_id=nft_id)

def unassoc_pet(request, nft_id, pet_id):
  Nft.objects.get(id=nft_id).pets.remove(pet_id)
  return redirect('detail', nft_id=nft_id)