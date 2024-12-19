from orders.models import NotificationAboutRobotAvailability


class NotificationAboutRobotAvailabilityDAO:
    _model = NotificationAboutRobotAvailability

    def update_or_create_notification(
        self, customer_id: int, order_id: int, is_notified: bool
    ) -> None:
        self._model.objects.update_or_create(
            customer_id=customer_id,
            order_id=order_id,
            defaults={
                "is_notified": is_notified,
            },
        )
