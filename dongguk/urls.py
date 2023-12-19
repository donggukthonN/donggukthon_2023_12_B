from django.contrib import admin
from django.urls import path, include
from login import views as login_views
from question import views as question_views
from final import views as final_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_views.Login.login,name='login'),
    path('signup/duplicate/',login_views.SignUpDuplicated.check_duplicate_user,name='duflicate'),
    path('signup/',login_views.SignUp.signup,name='signup'),
    path('<str:u_id>/question/<int:q_id>/',question_views.ShowQuestion.show_question,name="show_question"),
    path('<str:u_id>/question/<int:q_id>/answer/',question_views.PostAnswer.post_answer,name="post_answer"),
    path('<str:u_id>/question/calendar/<int:q_id>/',question_views.GetCalendar.get_calendar,name="get_calendar"),
    path('<str:u_id>/question/calendar/<int:q_id>/correct/',question_views.PutCalendar.put_calendar,name="put_calendar"),
    path('<str:u_id>/final/profile/',final_views.Profile.profile,name="profile"),
    path('<str:u_id>/final/book/',final_views.UserBook.user_book,name='book'),
    path('<str:u_id>/final/friend/',final_views.GetFriend.get_friend,name="friend"),
    path('<str:u_id>/final/friend/add/',final_views.AddFriend.add_friend,name="add_friend"),
    path('<str:u_id>/final/friend/delete/<str:f_id>/',final_views.DeleteFriend.delete_friend,name="delete_friend"),
    path('<str:u_id>/final/friend/<str:f_id>/book/',final_views.FriendBook.friend_book,name="friend_book"),
]
