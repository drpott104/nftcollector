from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('nfts/', views.nfts_index, name='index'),
    path('nfts/<int:nft_id>/', views.nfts_detail, name='detail'),
    path('nfts/create', views.NftCreate.as_view(), name='nfts_create'),
    path('nfts/<int:pk>/update', views.NftUpdate.as_view(), name='nfts_update'),
    path('nfts/<int:pk>/delete', views.NftDelete.as_view(), name='nfts_delete'),
    path('nfts/<int:nft_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('pets/<int:nft_id>/assoc_pet/<int:pet_id>/', views.assoc_pet, name='assoc_pet'),
    path('pets/<int:nft_id>/unassoc_pet/<int:pet_id>/', views.unassoc_pet, name='unassoc_pet'),
    path('pets/', views.PetList.as_view(), name='pets_index'),
    path('pets/<int:pk>/', views.PetDetail.as_view(), name='pets_detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
]