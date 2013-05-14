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

@csrf_exempt
def task_view(request, *args, **kwargs):
    if request.method == 'GET':
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
	elif request.method == 'POST':
		if request.is_ajax():
			return render_to_response("task.html", json.dumps({'message' : 'awesome'},
				ensure_ascii=False), mimetype='application/javascript')
	raise Http404   



           
    
