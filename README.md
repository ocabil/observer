A simple MicroPython implementation of the Observer design pattern using decorators.

## Features

- For `async` or `def` functions
- Easy to extend and maintain

## Usage

```python
from observer import dispatch, enroll

@enroll("test")
async def asyncFunction(data: dict):
    print(f"`asyncFunction` data={data}")
    await asyncio.sleep(0.1)


@enroll("test")
def function(data: dict):
    print(f"`function` data={data}")

dispatch(event="test", data={"message": "This is a test"})
```

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

See `test.py` for a detail example
