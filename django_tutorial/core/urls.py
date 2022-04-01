from django.urls import path
from django_tutorial.core.views import index, detail, results, vote

app_name = 'core'
urlpatterns = [
    # ex: /polls/
    path('', index, name='index'),
    # ex: /polls/5/
    path('specifics/<int:question_id>/', detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
]
