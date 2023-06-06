from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class AddToppingHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "extra-topping":
            return f"Extra toping was added {request}"
        else:
            return super().handle(request)


class RemoveToppingHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Remove":
            return f"The {request} was removed"
        else:
            return super().handle(request)


class OrderHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Order":
            return f"The  {request} was made"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:


    for request in ["extra-topping", "Remove", "Order"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(request)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {request} was left untouched.", end="")



