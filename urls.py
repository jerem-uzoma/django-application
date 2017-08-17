urls.py


# add to the top
from collection import views

urlpatterns = [
    url(r'^$', views.index, name='Form'),
    # new url definition
    url(r'^list/$', views.contact, name='Post Lists')
