import asyncio
import random

import observer


@observer.enroll("test")
async def async_handler(data: dict):
    print(f"`async_handler` data={data}")
    await asyncio.sleep(0.1)


@observer.enroll("test")
def handler(data: dict):
    print(f"`handler` data={data}")


# Custom decorator using observer.enroll
def test(_handler):
    return observer.enroll("test")(_handler)


@test
def f(data: dict):
    print(f"`{f.__name__}` data={data}")


def random_data() -> dict:
    return {
        "args": [random.randint(0, 100) for _ in range(random.randint(1, 4))],
        "kwargs": {
            chr(random.randint(0, 0x10FFFF)): random.randint(0, 100)
            for _ in range(random.randint(1, 4))
        },
    }


def random_dict():
    return {
        chr(random.randint(0, 0x10FFFF)): random.randint(0, 100)
        for _ in range(random.randint(1, 4))
    }


def random_list():
    return [random.randint(0, 100) for _ in range(random.randint(1, 4))]


_data: dict = random_data()

# Dispatch
print(f"Dispatching event='test' with data={_data}")
observer.dispatch(event="test", data=_data)
print()

# Erase
print(f"Erasing handler={handler.__name__}")
erased: bool = observer.erase(event="test", handler=handler)
print(f"erased={erased}")
print()

# Dispatch
_data: dict = random_data()
print(f"Dispatching event='test' with data={_data} after erasing `{handler.__name__}`")
observer.dispatch(event="test", data=_data)
print()

print("Goodbye!")
