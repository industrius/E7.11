from django.urls import path
from .views import AdvertList, AdvertDetail, CommentCreate, TagCreate, GetStat
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(10)(AdvertList.as_view())),
    path('<int:pk>', cache_page(10)(AdvertDetail.as_view())),
    path('comment', CommentCreate.as_view()),
    path('tag', TagCreate.as_view()),
    path('stat/<int:pk>', cache_page(10)(GetStat.as_view()))
]