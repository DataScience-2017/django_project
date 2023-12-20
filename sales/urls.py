from django.urls import path
from .views import 교육목록, 세일상세, 세일_입력, 세일_업데이트, 세일_지우기

app_name ='홈페이지' # 아무거나로 써도 실행은 됨

urlpatterns = [
    path('', 교육목록, name='목록'),
    path('<int:pk>/', 세일상세, name='상세'), # 무조건 pk(primary key)로 설정해야함. 정해진것.
    path('mamonde/', 세일_입력, name='생성'),
    path('<int:pk>/업데이트', 세일_업데이트,name='업뎃'),
    path('<int:pk>/지우기', 세일_지우기, name='지우기'),
]