from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm


# Create your views here.

class TodoListView(ListView):
    model = Todo
    template_name = 'todo/list.html'
    context_object_name = "todo_list"
    paginate_by = 5


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/create.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo:main')


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo/update.html'
    fields = ('title', 'description', 'completed')
    success_url = reverse_lazy('todo:main')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:main')
    template_name = 'todo/delete.html'


