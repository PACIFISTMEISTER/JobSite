from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Candidate
from Auth.models import GetAllCandidates


class ShowAll(ListView):
    """отображение всех соискателей"""
    model = Candidate
    paginate_by = 1
    template_name = 'template/candidate.html'
    def get_queryset(self):

        return GetAllCandidates()


class ShowCandidate(DetailView):
    """отображение конкретного соискателя"""
    model = Candidate
    template_name = 'template/candidate_info.html'

