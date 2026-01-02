from typing import TypeVar, Optional
from counter import CountedList, Ops, lt, gt, eq

T = TypeVar("T")

def binary_search(arr: CountedList[T], target: T, ops: Ops) -> Optional[int]:
    low = 0
    high = len(arr) - 1

    while low <= high:
        ops.loops += 1

        mid = (low + high) // 2
        value = arr[mid]

        if eq(value, target, ops):
            return mid
        elif lt(value, target, ops):
            low = mid + 1
        else:
            high = mid - 1

    return None
