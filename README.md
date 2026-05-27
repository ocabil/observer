A simple MicroPython implementation of the Observer design pattern using decorators.

## Features

- For `async` or `def` functions
- Easy to extend and maintain

## Usage

```python
import asyncio

from observer import dispatch, enroll


@enroll("test")
async def async_handler(data: dict):
    print(f"`async_handler` data={data}")
    await asyncio.sleep(0.1)


@enroll("test")
def handler(data: dict):
    print(f"`handler` data={data}")


dispatch(event="test", data={"message": "This is a test"})
```

Use the similar `adispatch` function when you want the event to be delivered asychronously.

### Custom Decorator

```python
from random import randint
from observer import dispatch, enroll


def notify(handler):
    """
    `@notify` Decorator
    """
    return enroll(event="notify")(handler)


@notify
def setup(data: dict):
    print(f"{setup.__name__} has received data={data}!")


dispatch(event="notify", data={chr(randint(0, 0x10FFFF)): randint(0, 100)})
```

See `test.py` for a detailed example
