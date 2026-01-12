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




"""
TODO:
- simulate_card_game 구현하기
    # 카드 게임 시뮬레이션 구현
        # 1. 큐 생성
        # 2. 카드가 1장 남을 때까지 반복
        # 3. 마지막 남은 카드 반환
"""


def simulate_card_game(n: int) -> int:
    """
    카드2 문제의 시뮬레이션
    맨 위 카드를 버리고, 그 다음 카드를 맨 아래로 이동
    """
    # 구현하세요!
    queue = create_circular_queue(n)

    while len(queue) > 1:
        _ = queue.popleft()  # 1번을 버림
        value = queue.popleft()  # 2번을 pop
        queue.append(value)  # 2번을 맨 아래로 옮김

    return queue.pop()

def solve_card2() -> None:
    """입, 출력 format"""
    n: int = int(input())
    result: int = simulate_card_game(n)
    print(result)

if __name__ == "__main__":
    solve_card2()