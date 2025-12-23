import asyncio
import random

import observer


@observer.enroll("test")
async def asyncFunction(data: dict):
    print(f"`asyncFunction` data={data}")
    await asyncio.sleep(0.1)


@observer.enroll("test")
def function(data: dict):
    print(f"`function` data={data}")


# Custom decorator using observer.enroll
def test(handler):
    return observer.enroll("test")(handler)


@test
def f(data: dict):
    print(f"`{f.__name__}` data={data}")


def randomData() -> dict:
    return {
        "args": [random.randint(0, 100) for _ in range(random.randint(1, 4))],
        "kwargs": {
            chr(random.randint(0, 0x10FFFF)): random.randint(0, 100)
            for _ in range(random.randint(1, 4))
        },
    }


def randomDict():
    return {
        chr(random.randint(0, 0x10FFFF)): random.randint(0, 100)
        for _ in range(random.randint(1, 4))
    }


def randomList():
    return [random.randint(0, 100) for _ in range(random.randint(1, 4))]


# Dispatch
data: dict = randomData()
print(f"Dispatching event='test' with data={data}")
observer.dispatch(event="test", data=data)
print()

# Erase
print(f"Erasing handler={function.__name__}")
erased: bool = observer.erase(event="test", handler=function)
print(f"erased={erased}")
print()

# Dispatch
data: dict = randomData()
print(f"Dispatching event='test' with data={data} after erasing `{function.__name__}`")
observer.dispatch(event="test", data=data)
print()

print("Goodbye!")
