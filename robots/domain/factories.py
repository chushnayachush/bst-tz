from .daos.robot_dao import RobotDAO
from .usecases.create_robot_usecase import CreateRobotUsecase


def get_create_robot_usecase() -> CreateRobotUsecase:
    return CreateRobotUsecase(
        robot_dao=RobotDAO(),
    )
