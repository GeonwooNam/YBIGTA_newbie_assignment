from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    # 구현하세요!
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline

    MAX_TASTE = 1_000_000  # 맛 범위: 1 ~ 1,000,000
    n = int(input().strip())

    # 이 문제는 "합(카운트) 세그먼트 트리"로 처리 가능
    # - identity: 0 (합의 항등원)
    # - merge: a + b
    # - lift: 리프 값(T=int)을 그대로 U=int로 사용
    # - default: 초기 리프 값 0 (처음 사탕상자는 비어있음)
    st = SegmentTree[int, int](
        MAX_TASTE,
        identity=0,
        merge=lambda a, b: a + b,
        lift=lambda x: x,
        default=0,
    )

    out_lines: list[str] = []

    for _ in range(n):
        parts = input().split()
        a = int(parts[0])

        if a == 1:
            # 1 B: 사탕상자에서 B번째로 맛있는 사탕을 꺼낸다
            k = int(parts[1])

            # k번째 사탕의 맛(0-based 인덱스)을 찾는다
            idx = st.find_kth(k)

            # 출력은 1-based 맛 번호
            out_lines.append(str(idx + 1))

            # 해당 맛 사탕 1개 제거
            def dec(x: int) -> int:
                return x - 1

            st.update_apply(idx, dec)

        else:
            # 2 B C: 맛 B 사탕을 C개 추가(양수)/제거(음수)
            taste = int(parts[1])
            delta = int(parts[2])

            # taste는 1-based이므로 0-based로 변환
            def add(delta: int):
                def f(x: int) -> int:
                    return x + delta
                return f

            st.update_apply(taste - 1, add(delta))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()