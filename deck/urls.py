from django.urls import path
from . import views

urlpatterns = [
    path('board/<int:board_id>/', views.board_view, name='board'),
    path('column/<int:column_id>/add_task/', views.add_task, name='add_task'),
    path('move_task/', views.move_task, name='move_task'),
]