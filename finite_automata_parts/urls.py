from django.urls import path
from . import views
import constants

# Define the name of this app
app_name = 'fa'


urlpatterns = [
    path(constants.URL_FA_CREATE, views.create.as_view(), name='create'),
    path(constants.URL_FA_CHECK, views.check.as_view(), name='check'),
    path(constants.URL_FA_LONGEST_RUN, views.longest_run.as_view(), name='longest-run'),
    path(constants.URL_FA_REACHABLE, views.reachable.as_view(), name='reachable'),
    path(constants.URL_FA_PRODUCTIVE, views.productive.as_view(), name='productive'),
    path(constants.URL_FA_SIM_PAIRS, views.simulation_pairs.as_view(), name='sim-pairs'),
    path(constants.URL_FA_MINIMIZE, views.minimize.as_view(), name='minimize'),
    path(constants.URL_FA_STAR, views.star.as_view(), name='star'),
    path(constants.URL_FA_DETERMINE, views.determine.as_view(), name='determine'),
    path(constants.URL_FA_COMPLEMENT, views.complement.as_view(), name='complement'),
    path(constants.URL_FA_UNION, views.union.as_view(), name='union'),
    path(constants.URL_FA_CONCATENATE, views.concatenate.as_view(), name='concatenate'),
    path(constants.URL_FA_INTERSECT, views.intersect.as_view(), name='intersect'),
    path(constants.URL_FA_SYM_DIFF, views.symmetric_difference.as_view(), name='sym-diff'),
    path(constants.URL_FA_EQUIVALENT, views.equivalent.as_view(), name='equivalent'),
    path(constants.URL_FA_INCLUSION, views.inclusion.as_view(), name='inclusion'),
]
