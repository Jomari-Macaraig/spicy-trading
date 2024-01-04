from django.urls import path
from trading.journals.api import views as journals_views


urlpatterns = [
    path(
        route="journal/",
        view=journals_views.JournalList.as_view(),
        name="journal"
    ),
]