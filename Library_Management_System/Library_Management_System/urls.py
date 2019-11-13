"""Library_Management_System URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include("homepage.urls")),
    url(r'^booksearch/', include("booksearch.urls")),
    url(r'^checkinbooks/', include("checkinbooks.urls")),
    url(r'^addborrowers/', include("addborrowers.urls")),
    url(r'^payfine/', include("payfine.urls")),
]
