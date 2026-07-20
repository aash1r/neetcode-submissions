from typing import Any


def merge(a: dict[str, Any], b: dict[str, Any]):
    for x in b:
        result = b.get(x)
        if x not in a:
            a[x] = result
        elif result is not None:
            a[x] += result
    return a


def main():
    a = {"a": 10, "b": 20}
    b = {"b": 5, "c": 15}
    result = merge(a=a, b=b)
    print(result)


main()
