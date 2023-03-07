from import_export import resources
from jaiib.models import Question

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
