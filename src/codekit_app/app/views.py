# Create your views here.
from django.utils import simplejson
from django.views.generic import list_detail
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from app.models import Task, Block, Check, Language
import random
from app.check import * 

def task_view(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404


def task_view_get(request, *args, **kwargs):
    assert request.method == 'GET'
    try:
		taskId = int(args[0])
    except taskId.DoesNotExist:
        raise Http404
    try:
        task= Task.objects.get(id = taskId)
    except Task.DoesNotExist:
        raise Http404
    return list_detail.object_list(
        request,
        queryset = Block.objects.filter(task = taskId),
        template_name = "task.html",
        extra_context = {"task" : task}
	)    


def task_view_post(request, *args, **kwargs):
	assert request.method == 'POST'
	taskId = int(args[0])
	solution = request.POST.get("code")		
	inputs_outputs = Check.objects.filter(task = taskId)
	langId  =  Language.objects.get(task__id__exact = taskId)['accessId']
	return HttpResponse(simplejson.dumps(checkSolution(solution, inputs_outputs, langId), ensure_ascii=False), mimetype='application/javascript')
