
from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('test/', views.test_api_view),

    path('directors/', views.DirectorListView.as_view()),
    path('directors/<int:pk>/', views.DirectorDetailView.as_view()),

    path('movies/', views.MovieListView.as_view()),
    path('movies/<int:pk>/', views.MovieDetailView.as_view()),

    path('reviews/', views.ReviewListView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view()),

    path('movies/reviews/', views.MovieWithReviewsView.as_view(), name='movie-reviews'),
    path('average-rating/', views.AverageRatingView.as_view(), name='average-rating'),

    path('directors/movies-count/', views.DirectorWithMoviesCountView.as_view(), name='directors-movies-count'),

    path('directors/create/', views.DirectorCreateView.as_view(), name='director-create'),
    path('directors/<int:pk>/', views.DirectorUpdateDeleteView.as_view(), name='director-update-delete'),
    path('movies/create/', views.MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', views.MovieUpdateDeleteView.as_view(), name='movie-update-delete'),
    path('reviews/create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', views.ReviewUpdateDeleteView.as_view(), name='review-update-delete'),
]
