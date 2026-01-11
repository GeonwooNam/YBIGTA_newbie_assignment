from lib import Trie
import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    # 구현하세요!
    # 빠른 입력을 위해 전체 데이터를 한 번에 읽음
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    names = sorted(input_data[1:])

    trie: Trie[int] = Trie()

    for name in names:
        trie.push(name)

    # 팩토리얼 미리 계산
    mod = 1_000_000_007
    fact = [1] * (n + 2)
    for i in range(2, n + 2):
        fact[i] = (fact[i - 1] * i) % mod

    # Trie 쪽에 구현해 둔 정답 계산 메서드 호출
    print(trie.count_orders(fact))


if __name__ == "__main__":
    main()