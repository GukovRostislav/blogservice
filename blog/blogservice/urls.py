from django.urls import path
from .views import *

urlpatterns = [
    path('',
         index,
         name='main'),

    path('about/',
         about),

    path("create/",
         create,
         name='create_post'),

    path("create/",
         create,
         name='post_add'),

    path("sign-in/",
         sign_in,
         name='sign_in'),

    path("sign-in/",
         sign_in,
         name='sign_in_e'),

    path("delete-cookie/",
         log_out,
         name='log_out'),

    path("sign-up/",
         sign_up,
         name='sign_up'),

    path("sign-up/",
         sign_up,
         name='sign_up_e'),

    path("personal-area/",
         personal_area,
         name='personal_area_p'),

    path("post/<int:id>/",
         show_post,
         name='post_show'),

    path("post/<int:id>/",
         show_post,
         name='add_comment'),

    path("post/<int:id>/edit/",
         edit_post,
         name='post_edit'),

    path("users/<str:login>/",
         check_unique_login,
         name='check-unique-login'),

    path("likes/<int:user_id>/<int:post_id>",
         check_post_liked,
         name='check-is-post-liked'),
]
