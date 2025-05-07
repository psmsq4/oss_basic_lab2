from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Project, Choice, ScoreAggregation

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'project/index.html'
    context_object_name = 'all_portfolio_list'

    def get_queryset(self):
        return Project.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Project
    template_name = 'project/detail.html'

class ResultsView(generic.DetailView):
    model = Project
    template_name = 'project/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()

        context['scoreAgg'] = project.scoreaggregation_set.all()[0]

        return context

def vote(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    scoreAgg = get_object_or_404(ScoreAggregation, project=project)

    try:
        selected_choice = project.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'project/detail.html', {
            'project': project,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.eval_agg += 1
        selected_choice.save()

        scoreAgg.total_votes = sum(c.eval_agg for c in project.choice_set.all())
        scoreAgg.total_scores = sum((i+1) * c.eval_agg for i, c in enumerate(project.choice_set.all()))
        scoreAgg.average_scores = round(scoreAgg.total_scores / scoreAgg.total_votes, 2) if scoreAgg.total_votes > 0 else 0 
        scoreAgg.save()

        return HttpResponseRedirect(reverse('project:results', args=(project.id,)))

