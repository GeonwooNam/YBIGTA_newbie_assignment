# lib.py의 Matrix 클래스를 참조하지 않음
import sys


"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    분할 정복(Divide and Conquer)을 이용해 거듭제곱 연산을 빠르게 수행합니다.
    지수를 절반씩 줄여나가며 계산하여 시간 복잡도를 $O(\log \text{exp})$로 최적화합니다.

    Args:
        - base (int): 거듭제곱할 밑수.
        - exp (int): 지수 (0 이상의 정수).
        - mod (int): 나머지 연산을 수행할 값 (나머지 법).

    Returns:
        - result (int): (base^exp) % mod 연산의 결과값.
    """
    # 구현하세요!
    # base^0에 도달 시 1 반환
    if exp == 0:
        return 1

    # 지수를 절반으로 나누어 계산 (O(log N))
    half = fast_power(base, exp // 2, mod)
    result = (half * half) % mod

    # 지수가 홀수라면 base를 한 번 더 곱해줌
    if exp % 2 == 1:
        result = (result * base) % mod

    return result

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 

if __name__ == "__main__":
    main()
