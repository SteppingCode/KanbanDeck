from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Board, Column, Task
import json


def board_view(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    return render(request, 'board.html', {'board': board})


def add_task(request, column_id):
    column = get_object_or_404(Column, id=column_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(column=column, title=title, order=column.tasks.count())
    return redirect('board', board_id=column.board.id)


def move_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id')
        column_id = data.get('column_id')

        task = Task.objects.get(id=task_id)
        task.column_id = column_id
        task.save()

        return JsonResponse({'status': 'ok'})