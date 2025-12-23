import asyncio
import random

import observer


@observer.enroll("test")
async def asyncFunction(payload: dict):
    print(f"`asyncFunction` payload={payload}")
    await asyncio.sleep(0.1)


@observer.enroll("test")
def function(payload: dict):
    print(f"`function` payload={payload}")


def randomList():
    return [random.randint(0, 100) for _ in range(random.randint(1, 4))]


def randomDict():
    return {
        chr(random.randint(0, 0x10FFFF)): random.randint(0, 100)
        for _ in range(random.randint(1, 4))
    }


# Dispatch
observer.dispatch(event="test", payload={"args": randomList(), "kwargs": randomDict()})

# Erase
erased: bool = observer.erase(event="test", handler=function)
print(f"`function` erased={erased}")

# Dispatch
observer.dispatch(event="test", payload={"args": randomList(), "kwargs": randomDict()})

print("Goodbye!")
