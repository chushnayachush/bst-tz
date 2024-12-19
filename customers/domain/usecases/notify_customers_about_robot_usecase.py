from django.conf import settings
from django.core.mail import send_mail

from orders.domain.daos.orders_dao import OrderDAO
from robots.domain.daos.robots_dao import RobotDAO
from orders.domain.daos.notification_about_robot_availability_dao import (
    NotificationAboutRobotAvailabilityDAO,
)

from customers.domain import constants


class NotifyCustomersAboutRobotUsecase:
    def __init__(
        self,
        robots_dao: RobotDAO,
        orders_dao: OrderDAO,
        notification_about_robot_dao: NotificationAboutRobotAvailabilityDAO,
    ) -> None:
        self._robots_dao = robots_dao
        self._orders_dao = orders_dao
        self._notification_about_robot_dao = notification_about_robot_dao

    def execute(self, robot_id: int) -> None:
        robot_entity = self._robots_dao.get_robot_by_id(robot_id=robot_id)
        if robot_entity:
            payload_iterator = (
                self._orders_dao.get_customers_info_and_order_ids_by_serial(
                    serial=robot_entity.serial
                )
            )
            for payload in payload_iterator:
                res = send_mail(
                    constants.ROBOT_NOTIFICATION_SUBJECT.format(
                        version=robot_entity.version, model=robot_entity.model
                    ),
                    constants.ROBOT_NOTIFICATION_MESSAGE_BODY.format(
                        model=robot_entity.model, version=robot_entity.version
                    ),
                    settings.EMAIL_SENT_FROM,
                    [payload["customer__email"]],
                    fail_silently=True,
                )

                self._notification_about_robot_dao.update_or_create_notification(
                    customer_id=payload["customer_id"],
                    order_id=payload["id"],
                    is_notified=bool(res),
                )
