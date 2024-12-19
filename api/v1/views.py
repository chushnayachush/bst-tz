import json

from django import views
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from robots.forms import RobotForm
from robots.domain.entities import CreateRobotRequestEntity
from robots.domain.factories import get_create_robot_usecase


@method_decorator(csrf_exempt, name="dispatch")
# так лучше не делать, особенно когда форму используем, но для данного случая ок, потому что нет авторизации
class CreateRobotAPIView(views.View):
    _usecase = get_create_robot_usecase()

    def post(self, request: HttpRequest):
        form = RobotForm(json.loads(request.body))
        if form.is_valid():
            create_robot_entity = CreateRobotRequestEntity(**form.cleaned_data)
            try:
                status_code, data = (
                    200,
                    self._usecase.execute(
                        create_robot_entity=create_robot_entity
                    ).as_dict(),
                )
            except Exception as e:
                status_code, data = 400, str(e)

        else:
            status_code, data = 400, form.errors.get_json_data()

        return JsonResponse(status=status_code, data=data)


create_robot_apiview = CreateRobotAPIView.as_view()
