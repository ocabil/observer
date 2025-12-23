"""
Observer pattern implementation using decorators for event-driven programming.

This module provides a simple enroll-dispatch mechanism for event handling,
supporting both synchronous and asynchronous handlers.
"""

import asyncio

_enrolled: dict[str, set] = {}


def enroll(event: str):
    """
    Decorator to register a handler function for a specific event.
    It supports both synchronous and asynchronous functions.

    .. code-block:: python

        from observer import enroll

        @enroll("event")
        def handler(data: dict):
            print(f"{handler.__name__} received data: {data}")
    """

    def decorator(handler):
        _enrolled.setdefault(event, set()).add(handler)
        return handler

    return decorator


def erase(event: str, handler) -> bool:
    """
    Remove an enrolled handler from an event, if present.
    """
    try:
        _enrolled.get(event, set()).remove(handler)
        return True
    except KeyError:
        return False


def dispatch(event: str, data: dict) -> None:
    """
    Calls all handlers enrolled for a given event.
    """

    def _asynchronous(handler) -> bool:
        return type(handler) is not type(lambda: None)

    for enrollee in _enrolled.get(event, set()):
        if _asynchronous(enrollee):
            asyncio.run(enrollee(data=data))
        else:
            enrollee(data=data)
