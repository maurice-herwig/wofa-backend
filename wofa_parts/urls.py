from django.urls import path
from . import views
import constants

urlpatterns = [
    path(constants.URL_WOFA_WEIGHT, views.weight.as_view()),
    path(constants.URL_WOFA_WEIGHT_DIFF, views.weight_diff.as_view()),
    path(constants.URL_WOFA_GRADING_WEIGHT, views.grading_weight.as_view()),
    path(constants.URL_WOFA_GRADING_SUBSETS, views.grading_subsets.as_view()),
    path(constants.URL_WOFA_GRADING_TEST_WORDS, views.grading_test_words.as_view()),
]
