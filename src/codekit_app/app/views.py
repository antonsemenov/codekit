# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from app.models import Task
def task_view(request, lang, task_id):
    try:
        lang = str(lang)
        task_id = int(task_id)
    except ValueError:
        raise Http404()

    cur_task = Task.objects.filter(lang=lang, id=task_id)
    return render_to_response('task.html', {'html_block': cur_task})
