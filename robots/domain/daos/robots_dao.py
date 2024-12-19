from datetime import datetime
from dataclasses import dataclass

from robots.models import Robot


@dataclass(frozen=True)
class RobotEntity:
    serial: str
    version: str
    model: str
    created: datetime


class RobotDAO:
    _model = Robot

    def _to_entity(self, robot: Robot | None) -> RobotEntity | None:
        if robot:
            return RobotEntity(
                serial=robot.serial,
                version=robot.version,
                model=robot.model,
                created=robot.created,
            )

    def get_robot_by_id(self, robot_id: int) -> RobotEntity | None:
        return self._to_entity(self._model.objects.filter(id=robot_id).last())
