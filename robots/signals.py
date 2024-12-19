from typing import Type, Any

from django.db.models.signals import post_save

from robots.models import Robot
from customers.domain.factories import get_notify_customers_about_robot_usecase


def notify_about_robot_availability(
    sender: Type[Robot], instance: Robot, created: bool, **kwargs: Any
) -> None:
    if created:
        usecase = get_notify_customers_about_robot_usecase()
        usecase.execute(instance.pk)


post_save.connect(
    notify_about_robot_availability,
    sender=Robot,
    dispatch_uid="notify_about_robot_availability",
)
