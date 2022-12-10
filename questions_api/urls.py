from django.urls import include, path

from rest_framework import routers

from questions_api.views import *

router = routers.DefaultRouter()
router.register(r'question', QuestionsViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('check_answers/', check_answer, name="check_answer"),
   path('send_username_mail/', send_username_mail, name="send_username_mail")
]