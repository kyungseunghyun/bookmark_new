from django.shortcuts import render

# Create your views here.
# CRUD를 할 줄 알아야 한다.
# LIST

# 클래스형 뷰(제레닉 뷰, 또는 공통 뷰), 함수형 뷰(내멋대로)
# 제레닉 뷰를 사용해여 개발한다.
# 제네닉 뷰를 사용하기 위해서는 import 한다.
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답을 한다.(화면을 본다)
# 응답해줄 View를 개발하는 것이다.

# 사용자가 어떤 URL를 넣었을 때 View를 보여주냐
# -> url.py에 정한다.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    #success_url = reverse_lazy('list')

    # 밑에 없으면 bookmark_form을 불러옴
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list') #삭제후 성공