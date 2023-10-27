from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
def createShowView(request):

    if request.method == 'POST':
        showForm = forms.TvShowForm(request.POST, request.FIELS)
        if showForm.is_valid()
            showForm.save()
            return HttpResponse('Успешно добавлен <a href="/"> На главную </a> ')
    else:
        showForm = forms.TvShowForm()
    return  render(request, template_name:'crud/create_film.html', context: {'from': showForm})

def deleteListView(request):
    if request.method == 'GET':
        show = models.TvShow.objects.all()
        context = {
            'show_key': show,
        }
        html_name = 'crud/del_film_list.html'
        return render(request, html_name, context)


def dropFilmView(request, id):
    film_id = get_object_or_404(models.TvShow, id=id)
    film_id.delete()
    return HttpResponse('Успешно удален <a href="/"> На главную </a> ')

def editFilmView(request, id):
    film_id = get_object_or_404(models.TvShow, id=id)
    if request.method == 'POST':
        form = forms.TvShowForm(instance=film_id, data=request.POST)
        if forms.is_valid():
            form.save()
            return HttpResponse('Успешно изменен <a href="/"> На главную </a> ')
    else:
        from = forms.TvShowForm(instance=film_id)
    context = {
        'film_key':film_id,
        'form':form,
    }
    return render(request, template_name:'crud/edit.html', context)



def updateListView(request):
        if request.method == 'GET':
            show = models.TvShow.objects.all()
            context = {
                'show_key': show,
            }
            html_name = 'crud/del_film_list.html'
            return render(request, html_name, context)




def tvShowListView(request):
    if request.method == 'GET':
        show = models.TvShow.objects.all()
        context = {
            'show_key': show,
        }
        html_name = 'tvshow/tvshow.html'
        return render(request, html_name, context)

def tvShowDetailView(request, id):
    show_id = get_object_or_404(models.TvShow, id=id)
    context = {
        'show_id_key':show_id,
    }
    html_detail_name = 'tvshow/tvshow_deteil.html'
    return render(request, html_detail_name, context)


