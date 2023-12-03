"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test_api_view),

    path('api/v1/directors/', views.DirectorListView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailView.as_view()),

    path('api/v1/movies/', views.MovieListView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailView.as_view()),

    path('api/v1/reviews/', views.ReviewListView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailView.as_view()),

    path('api/v1/movies/reviews/', views.MovieWithReviewsView.as_view(), name='movie-reviews'),
    path('api/v1/average-rating/', views.AverageRatingView.as_view(), name='average-rating'),

    path('api/v1/directors/movies-count/', views.DirectorWithMoviesCountView.as_view(), name='directors-movies-count'),

    path('api/v1/directors/create/', views.DirectorCreateView.as_view(), name='director-create'),
    path('api/v1/directors/<int:pk>/', views.DirectorUpdateDeleteView.as_view(), name='director-update-delete'),
    path('api/v1/movies/create/', views.MovieCreateView.as_view(), name='movie-create'),
    path('api/v1/movies/<int:pk>/', views.MovieUpdateDeleteView.as_view(), name='movie-update-delete'),
    path('api/v1/reviews/create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('api/v1/reviews/<int:pk>/', views.ReviewUpdateDeleteView.as_view(), name='review-update-delete'),
]
