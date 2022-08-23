from django.urls import path
from . import views
from .views import WorkOrderList, WorkOrderDetail, step1, step2, step3

# App urls

urlpatterns = [
    path('', WorkOrderList.as_view(), name='repair-home'),
    path('workorder/<int:pk>/', WorkOrderDetail.as_view(), name='workOrder-detail'),

    path('step1/', step1, name='step1'),
    path('step2/', step2, name='step2'),
    path('step3/', step3, name='step3'),
]
