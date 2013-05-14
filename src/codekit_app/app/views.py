# Create your views here.
from django.views.decorators.csrf import csrf_exempt

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
        lang = str(args[0])
        task_id = int(args[1])
    except ValueError:
        raise Http404()
    try:
        task= Task.objects.get(id = task_id)
    except Task.DoesNotExist:
        raise Http404
	
    return list_detail.object_list(
        request,
        queryset = Block.objects.all(),
        template_name = "task.html",
        extra_context = {"task" : task}
	)    

@csrf_exempt
def task_view_post(request, *args, **kwargs):
    if request.is_ajax():
        return HttpResponse(json.dumps({'message' : 'awesome'},
            ensure_ascii=False), mimetype='application/javascript')



#    assert request.method == 'POST'
#	json = simplejson.dumps('Hello')
#	return HttpResponse(json, mimetype='application/json')
    
