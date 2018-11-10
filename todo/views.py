from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import to_do_item

# Create your views here.

def todo_view(request):
	full_to_do_list = to_do_item.objects.all()
	return render(request, 'todo.html',
					      {'to_do_list' : full_to_do_list})

def add_todo_item(request):
	#accept the new item to do, save to DB and redirect back to base url

	new_to_do_item = to_do_item(content=request.POST['item'])
	new_to_do_item.save()
	return HttpResponseRedirect('/todo/')


def delete_todo_item(request, item_id):
	#accept id of item to be deleted, delete from Db and redirect back to base url
	to_do_item_to_del = to_do_item.objects.get(id=item_id)
	to_do_item_to_del.delete()
	return HttpResponseRedirect('/todo/')




