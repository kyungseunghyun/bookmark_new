from django.urls import path
from .views import * #BookmarkListView, BookmarkCreateView, BookmarkDetailView

urlpatterns = [
# http://127.0.0.1/bookmark/
    # 데이터까지 가져 왔다.
    path('',BookmarkListView.as_view(), name='list'), # as_view 함수형 view로 변환하여 보여준다.
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),

]