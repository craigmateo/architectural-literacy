from typing import Callable, Optional
from counter import CountedList, Ops
from linear_search import linear_search
from binary_search import binary_search

SearchFn = Callable[[CountedList[int], int, Ops], Optional[int]]

def run_case(
    name: str,
    data: list[int],
    target: int,
    search_fn: SearchFn
) -> None:
    ops = Ops()
    arr = CountedList(data, ops)
    result = search_fn(arr, target, ops)

    print(f"Algorithm: {name}")
    print(f"Data size: {len(data)}")
    print(f"Target: {target}")
    print(f"Result index: {result}")
    print(f"Ops: {ops}")
    print("-" * 40)

def main():
    data = list(range(0, 20))
    n = len(data)

    print("\n=== Linear Search ===")
    run_case("Best case", data, data[0], linear_search)
    run_case("Average-ish", data, data[n // 2], linear_search)
    run_case("Worst case", data, 999, linear_search)

    print("\n=== Binary Search ===")
    run_case("Best case", data, data[n // 2], binary_search)
    run_case("Average-ish", data, data[0], binary_search)
    run_case("Worst case", data, 999, binary_search)

if __name__ == "__main__":
    main()
