from django.http import HttpResponse, HttpResponseRedirect
from plantree.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext

def get(node_id):
    if node_id:
        return Category.objects.get(pk=node_id)
    return None

def redirect_for_node(node_id):
    return HttpResponseRedirect(reverse('plantree.views.treeview')
                                 + '%s/' % node_id)

def unfinished():
    return { 'finished' : False }
def finished():
    return { 'finished' : True }

def treeview(request, node_id=1):
    current_node = get(node_id)
    filter_name = request.session.get('filter_name', "")
    parent_node = current_node.get_parent()
    base_url = reverse('plantree.views.treeview')
    if filter_name:
        filter_func = eval(filter_name)()
    else:
        filter_func = {}

    child_list = current_node.get_children(filter=filter_func)
    return render_to_response('treeview.html',
                              {'current' : current_node,
                               'parent' : parent_node,
                               'child_list' : child_list,
                               'base_url' : base_url,
                               'request' : request, },
                              context_instance=RequestContext(request))

def filter(request, node_id):
    request.session['filter_name'] = request.POST['filter_name']
    return redirect_for_node(node_id)


def add(request, node_id):
    node = get_object_or_404(Category, pk=node_id)
    task = request.POST['task']
    child = node.add_child(task=task)
    return redirect_for_node(node_id)

def change(request, node_id):
    node = get_object_or_404(Category, pk=node_id)
    node.task = request.POST['new_task']
    node.save()
    return redirect_for_node(node_id)

def finish(request, node_id):
    node = get_object_or_404(Category, pk=node_id)
    parent_id = get(node_id).get_parent().id
    node.make_finished()
    node.save()
    return redirect_for_node(parent_id)

def unfinish(request, node_id):
    node = get_object_or_404(Category, pk=node_id)
    parent_id = get(node_id).get_parent().id
    node.make_unfinished()
    node.save()
    return redirect_for_node(parent_id)

def delete(request, node_id):
    node = get_object_or_404(Category, pk=node_id)
    parent_id = get(node_id).get_parent().id
    node.delete()
    return redirect_for_node(parent_id)
