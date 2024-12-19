from robots.domain.daos.robots_dao import RobotDAO
from robots.domain.usecases.export_robots_stat_usecase import ExportRobotsStatUsecase


def get_export_robots_stat_usecase() -> ExportRobotsStatUsecase:
    return ExportRobotsStatUsecase(
        robot_dao=RobotDAO(),
    )
