# noinspection PyPropertyDefinition
class AIOContext:
    def __init__(self, max_requests: int): ...

    @property
    def value(self) -> int: ...