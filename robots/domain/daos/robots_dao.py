import typing
from datetime import datetime, timedelta, timezone

from django.db import models
from django.utils.timezone import now, make_aware

from robots.models import Robot


class RobotStat(typing.TypedDict):
    model: str
    version: str
    count: int


class RobotDAO:
    _model = Robot

    def get_counts_grouped_by_model_and_version(
        self, created_from: datetime | None = None
    ) -> typing.Iterable[RobotStat]:
        if not created_from:
            created_from = datetime.now() - timedelta(days=7)

        created_from = make_aware(created_from)

        response = (
            self._model.objects.filter(created__gt=created_from)
            .values("model", "version")
            .annotate(count=models.Count("id"))
            .order_by("model", "version", "count")
            .iterator()
        )
        return response
