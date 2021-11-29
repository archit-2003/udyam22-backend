from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Workshop, NoticeBoard
from .serializers import WorkshopSerializer, NoticeBoardSerializer


class WorkshopView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WorkshopSerializer
    queryset = Workshop.objects.all().order_by('-date')


class GetAllNoticeView(generics.ListAPIView):
    serializer_class = NoticeBoardSerializer
    queryset = NoticeBoard.objects.all().order_by('-date')


class GetNoticeByIdView(generics.RetrieveAPIView):
    serializer_class = NoticeBoardSerializer
    queryset = NoticeBoard.objects.all()
    lookup_field = 'id'
