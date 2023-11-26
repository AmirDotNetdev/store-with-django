from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("products/",views.products,name='products'),
    path("logout/",views.logout,name='logout'),
    path("<int:id>product/",views.product,name='product'),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)