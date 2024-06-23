from random import randint
import asyncio


def printc(string: str, color="WHITE") -> None:
    color_dict = {
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "RED": "\033[91m",
        "WHITE": "\033[0m",
    }

    print(color_dict[color] + string + color_dict["WHITE"])


async def calculate(value: int) -> list[int]:
    if value < 1_000_000 or value > 20_000_000:
        raise ValueError

    return_value: list[int] = []

    for d in range(2, value // 2 + 1):
        if value % d == 0:
            return_value.append(d)

    return return_value


async def int_div(value: int):
    printc(f"\nValue: {value}")

    try:
        answer = await calculate(value)

    except ValueError:
        printc("Use number from 1.000.000 to 20.000.000", color="RED")

    else:
        if len(answer):
            print("\nList of integer dividers:")
            printc(f"{answer}\n", color="GREEN")
        else:
            printc(f"The number {value} is prime.\n", color="YELLOW")
    
        return answer


if __name__ == "__main__":
    asyncio.run(int_div(randint(1, 21_000_000)))
