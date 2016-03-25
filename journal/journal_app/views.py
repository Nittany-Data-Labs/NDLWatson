from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import JournalEntry

# Create your views here.
def index(request):
    journal_entry_list = JournalEntry.objects.all()
    context = {'journal_entry_list': journal_entry_list}
    return render(request, 'journal_app/index.html', context)


def detail(request, journal_entry_id):
    entry = get_object_or_404(JournalEntry, pk=journal_entry_id)
    return render(request, 'journal_app/detail.html', {'entry': entry})

def recordentry(request, journal_entry_id):
    response = "You're looking to record entry %s"
    return HttpResponse(response % journal_entry_id)
