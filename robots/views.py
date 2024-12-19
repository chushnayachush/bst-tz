import datetime

from django import views
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from robots.domain.factories import get_export_robots_stat_usecase


class ExportRobotsStatView(views.View):
    _usecase = get_export_robots_stat_usecase()
    FILENAME = "{dt}_export.xlsx"

    def get(self, request: HttpRequest) -> HttpResponse:
        tmp_buffer = self._usecase.execute()
        response = HttpResponse(content_type="application/vnd.ms-excel")
        filename = self.FILENAME.format(
            dt=datetime.datetime.now(tz=datetime.timezone.utc)
        )
        response["Content-Disposition"] = "attachment; filename={0}".format(filename)
        response.write(tmp_buffer)
        return response


export_robots_stat_view = ExportRobotsStatView.as_view()
