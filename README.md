A simple MicroPython implementation of the Observer design pattern using decorators.

## Features

- For `async` or `def` functions
- Easy to extend and maintain

## Usage

```python
from observer import dispatch, enroll

@enroll("test")
async def asyncFunction(payload: dict):
    print(f"`asyncFunction` payload={payload}")
    await asyncio.sleep(0.1)


@enroll("test")
def function(payload: dict):
    print(f"`function` payload={payload}")

dispatch(event="test", payload={"message": "This is a test"})
```

See `test.py` for a detail example
