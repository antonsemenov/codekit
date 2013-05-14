# Create your views here.
from django.views.generic import list_detail
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from app.models import Task, Block
try:
    import json
except ImportError:
    import simplejson


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
        task= Task.objects.get(id = 1)
    except Task.DoesNotExist:
        raise Http404
	
    return list_detail.object_list(
        request,
        queryset = Block.objects.all(),
        template_name = "task.html",
        extra_context = {"task" : task}
	)    


def task_view_post(request, *args, **kwargs):
	some_code = request.POST
	return HttpResponse(json.dumps(some_code, ensure_ascii=False), mimetype='application/javascript')

    
