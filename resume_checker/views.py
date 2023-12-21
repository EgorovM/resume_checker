from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from resume_checker.models import Vacancy, Resume
from resume_checker.recommendations.relevancy import get_score_and_edits
from resume_checker.serializers import VacancySerializer, ResumeSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class RelevancyView(APIView):
    def get(self, request, resume_id, vacancy_id):
        resume = get_object_or_404(id=resume_id, klass=Resume)
        vacancy = get_object_or_404(id=vacancy_id, klass=Vacancy)

        result = get_score_and_edits(vacancy.description, resume.content)
        return Response(result)


def index(request):
    return render(request, "index.html")
