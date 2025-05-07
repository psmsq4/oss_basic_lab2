from django.contrib import admin

from .models import Project, Choice, ScoreAggregation

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

    readonly_fields = ['eval_text', 'eval_agg']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_desc')
    search_field = ('project_name',)
    
    inlines=[ChoiceInline]

@admin.register(ScoreAggregation)
class ScoreAggregationAdmin(admin.ModelAdmin):
    list_diplay = ('project_name', 'project_desc', 'pub_date', 'average_scores', 'total_scores', 'total_votes')
    search_fields = ('project_name',)

    ordering = ['-average_scores']
    readonly_fields = ['average_scores', 'total_votes', 'total_scores']
