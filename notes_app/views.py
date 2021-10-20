from django.shortcuts import render, redirect
from apis.models import Note
from .forms import addNoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def myNotesList(request):
    context = {}
    notes = Note.objects.filter(user=request.user)
    context['notes'] = notes
    return render(request, 'note-list.html', context)

@login_required(login_url='login')
def addNote(request):
    context = {}
    form = addNoteForm
    if request.method == 'POST':
        note = Note.objects.create(
            user = request.user,
            title = request.POST.get('title'),
            body = request.POST.get('body')
        )
        return redirect('view-note', pk=note.pk)
    context['form'] = form
    return render(request, 'add-note.html', context)

@login_required(login_url='login')
def editNote(request, pk):
    note = Note.objects.get(pk = pk)
    form = addNoteForm(instance=note)
    if request.method == 'POST':
        form = addNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('view-note', pk=note.pk)
    context = {'form':form}
    return render(request, 'edit-note.html', context)

@login_required(login_url='login')
def viewNote(request, pk):
    context = {}
    note = Note.objects.get(pk = pk)
    context['note'] = note
    return render(request, 'view-note.html', context)

@login_required(login_url='login')
def deleteNote(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return redirect('notes-list')

@login_required(login_url='login')
def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('login')

    


