import typing
from orders.models import Order


class UserIdWithEmailAndOrderId(typing.TypedDict):
    id: int
    customer_id: int
    customer__email: str


class OrderDAO:
    _model = Order

    def get_customers_info_and_order_ids_by_serial(
        self, serial: str
    ) -> typing.Iterator[UserIdWithEmailAndOrderId]:
        return (
            self._model.objects.select_related("customer")
            .filter(robot_serial=serial)
            .values("customer_id", "id", "customer__email")
            .iterator()
        )
