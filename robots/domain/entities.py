from dataclasses import dataclass, asdict


class BaseEntity:
    def as_dict(self):
        return asdict(self)


@dataclass(frozen=True)
class CreateRobotRequestEntity(BaseEntity):
    model: str
    version: str
    created: str


@dataclass(frozen=True)
class RobotEntity(BaseEntity):
    id: int
    serial: str
    model: str
    version: str
    created: str
