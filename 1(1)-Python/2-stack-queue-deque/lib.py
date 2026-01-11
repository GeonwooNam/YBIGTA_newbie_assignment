from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove 구현하기 
"""


def create_circular_queue(n: int) -> deque[int]:
    """1부터 n까지의 숫자로 deque를 생성합니다."""
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    """
    큐에서 k번째 원소를 제거하고 반환합니다.
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