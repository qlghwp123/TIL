from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def todo_create(req):
    _content = req.GET.get('content')
    _priority = req.GET.get('priority')
    _deadline = req.GET.get('deadline')

    Todo.objects.create(content=_content, priority=_priority, deadline=_deadline).save()

    return redirect('todo:index')

def todo_read(req):
    db_data = Todo.objects.all().order_by('id')
    
    d = {'db_data': db_data}

    return render(req, 'todo/index.html', d)

def todo_update(req, _id):
    target = Todo.objects.get(id=_id)

    _content = req.POST['content']
    _priority = req.POST['priority']
    _deadline = req.POST['deadline']
    _completed = req.POST['completed']

    # maybe should check validation of these parameters
    # ...

    target.content = _content
    target.priority = _priority
    target.deadline = _deadline
    target.completed = _completed

    print(_content, _priority, _deadline, _completed)

    target.save()

    return redirect('todo:index')


def todo_delete(req, _id):
    target = Todo.objects.get(id=_id)

    target.delete()

    return redirect('todo:index')