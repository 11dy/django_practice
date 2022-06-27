from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    # """pybo/ URL은 다음처럼 config/urls.py 파일에 매핑된 pybo/ 와
    # pybo/urls.py 파일에 매핑된 '' 이 더해져 pybo/가 된다."""
    path('<int:question_id>/', views.detail, name ='detail'),
]