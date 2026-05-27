"""
Observer pattern implementation using decorators for event-driven programming.

This module provides a simple enroll-dispatch mechanism for event handling,
supporting both synchronous and asynchronous handlers.
"""

import asyncio

_enrolled: dict[str, set] = {}


async def adispatch(event: str, data: dict) -> None:
    """
    Asynchronously calls all handlers enrolled for a given event.
    """

    def _asynchronous(handler) -> bool:
        return type(handler) is not type(lambda: None)

    for enrollee in _enrolled.get(event, set()):
        if _asynchronous(enrollee):
            await enrollee(data=data)
        else:
            enrollee(data=data)


def dispatch(event: str, data: dict) -> None:
    """
    Calls all handlers enrolled for a given event.
    """
    return asyncio.run(adispatch(event=event, data=data))


def enroll(event: str):
    """
    Decorator used to register an asynchronous, or synchronous, handler function.
    Handler function should accept a single argument, `data`, which should be a dictionary.
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
