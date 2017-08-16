urls.py


# add to the top
from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    # new url definition
    url(r'^contact/$', views.contact, name='contact')
