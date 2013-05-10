# Create your views here.
from django.http import Http404, HttpResponse

def task_view(request, lang, task_id):
    try:
        lang = str(lang)
        task_id = int(task_id)
    except ValueError:
        raise Http404()
    html = '<html><body>This is %s anguage and task %s id!</body></html>' % (lang, task_id)
    return HttpResponse(html)
