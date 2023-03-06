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
]