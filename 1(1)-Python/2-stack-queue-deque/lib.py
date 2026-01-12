from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove 구현하기 
"""


def create_circular_queue(n: int) -> deque[int]:
    """
    1부터 n까지의 숫자로 deque를 생성합니다.

    Args:
        - n (int): 큐에 담을 최대 숫자. 1부터 n까지의 범위가 생성됩니다.

    Returns:
        - queue (deque[int]): 1부터 n까지의 정수가 담긴 deque 객체.
    """
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    """
    큐에서 k번째 원소를 찾아 제거하고 해당 값을 반환합니다.
    1번째부터 k-1번째까지의 원소는 회전하여 큐의 뒤로 이동합니다.

    Args:
        - queue (deque[int]): 숫자들이 저장된 순환 큐 객체.
        - k (int): 제거할 원소의 순서 (1-based index).

    Returns:
        - value (int): 큐에서 제거된 k번째 원소의 값.
    """
    value = None
    for i in range(k):
        value = queue.popleft()

        # 1 ~ k-1번재 원소 이동 (rotate)
        if i < k-1:
            queue.append(value)

        # k번째 원소 제거 및 반환 (remove)
        if i == k-1:
            return value

    # int 자료형 맞추어 반환
    return value if value is not None else 0