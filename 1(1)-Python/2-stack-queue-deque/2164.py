from lib import create_circular_queue


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