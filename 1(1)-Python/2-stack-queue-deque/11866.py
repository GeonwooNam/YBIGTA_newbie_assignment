from lib import create_circular_queue, rotate_and_remove


"""
TODO:
- josephus_problem 구현하기
    # 요세푸스 문제 구현
        # 1. 큐 생성
        # 2. 큐가 빌 때까지 반복
        # 3. 제거 순서 리스트 반환
"""


def josephus_problem(n: int, k: int) -> list[int]:
    """
    요세푸스 순열을 계산하여 반환합니다.
    1부터 n까지의 숫자가 원형으로 배치되어 있을 때, k번째 숫자를 반복적으로 제거하는 과정을 수행합니다.

    Args:
        - n (int): 전체 사람의 수 (1부터 n까지의 정수).
        - k (int): 매 단계마다 제거할 원소의 순서 (1-based index).

    Returns:
        - result (list[int]): 제거된 순서대로 숫자가 담긴 리스트 (요세푸스 순열).
    """
    # 구현하세요!
    # 1. 큐 생성
    queue = create_circular_queue(n)
    remove_list = []

    # 2. 큐가 빌 때까지 반복
    while len(queue) > 0:
        remove_value = rotate_and_remove(queue, k)
        remove_list.append(remove_value)

    # 3. 제거 순서 리스트 반환
    return remove_list

def solve_josephus() -> None:
    """입, 출력 format"""
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
    # 출력 형식: <3, 6, 2, 7, 5, 1, 4>
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    solve_josephus()