from robots.domain.daos.robot_dao import RobotDAO
from robots.domain.entities import CreateRobotRequestEntity, RobotEntity


class CreateRobotUsecase:
    def __init__(self, robot_dao: RobotDAO) -> None:
        self._robot_dao = robot_dao

    def execute(self, create_robot_entity: CreateRobotRequestEntity) -> RobotEntity:
        robot_entity = self._robot_dao.create_robot(
            create_robot_entity=create_robot_entity
        )
        return robot_entity
