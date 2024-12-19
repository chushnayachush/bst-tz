import typing

from robots.models import Robot
from robots.domain.entities import CreateRobotRequestEntity, RobotEntity


class RobotDAO:
    _model = Robot

    def create_robot(
        self, create_robot_entity: CreateRobotRequestEntity
    ) -> RobotEntity:
        robot_obj = self._model.objects.create(
            serial=f"{create_robot_entity.model}-{create_robot_entity.version}",
            model=create_robot_entity.model,
            version=create_robot_entity.version,
            created=create_robot_entity.created,
        )

        return RobotEntity(
            serial=robot_obj.serial,
            model=robot_obj.model,
            version=robot_obj.version,
            created=robot_obj.created,
        )
