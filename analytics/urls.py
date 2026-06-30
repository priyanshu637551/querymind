from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path("export/csv/", views.export_csv, name="export_csv"),
    path("history/<int:pk>/",views.report_detail,name="report_detail"),
]