from orders.domain.daos.orders_dao import OrderDAO
from robots.domain.daos.robots_dao import RobotDAO
from orders.domain.daos.notification_about_robot_availability_dao import (
    NotificationAboutRobotAvailabilityDAO,
)

from customers.domain.usecases.notify_customers_about_robot_usecase import (
    NotifyCustomersAboutRobotUsecase,
)


def get_notify_customers_about_robot_usecase() -> NotifyCustomersAboutRobotUsecase:
    return NotifyCustomersAboutRobotUsecase(
        robots_dao=RobotDAO(),
        orders_dao=OrderDAO(),
        notification_about_robot_dao=NotificationAboutRobotAvailabilityDAO(),
    )
