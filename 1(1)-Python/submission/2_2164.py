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
    N장의 카드가 있을 때, 마지막 한 장이 남을 때까지 카드를 버리고 옮기는 시뮬레이션을 수행합니다.
    1번 카드가 맨 위에, N번 카드가 맨 아래에 위치한 상태에서 시작하여
    맨 위 카드는 버리고, 그다음 카드는 맨 아래로 보내는 과정을 반복합니다.

    Args:
        - n (int): 초기 카드의 개수 (1부터 n까지의 정수).

    Returns:
        - last_card (int): 모든 과정을 마친 후 마지막으로 남게 되는 카드의 숫자.
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