from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model) :
    project_name = models.CharField(max_length=50)
    project_desc = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def save(self, *args, **kwargs):
        is_new = self.pk is None  
        super().save(*args, **kwargs)
        if is_new:
            for i in range(1, 6):
                Choice.objects.create(
                    project=self,
                    eval_text=f'score_{i}',
                    eval_agg=0
                )
            ScoreAggregation.objects.create(
                    project=self,
            )

    def __str__(self):
        return self.project_name

class Choice(models.Model) :
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    eval_text = models.CharField(max_length=20)
    eval_agg = models.IntegerField(default=0)

    def __str__(self):
        return self.eval_text

class ScoreAggregation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    total_scores = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    average_scores = models.FloatField(default=0)

    def __str__(self):
        return str(self.average_scores) + '_' + self.project.project_name
