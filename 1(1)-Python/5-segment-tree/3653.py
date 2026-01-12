from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    # 구현하세요!
    input = sys.stdin.readline

    t = int(input().strip())

    # n + m <= 200,000
    MAX_SIZE = 200_000

    # 이 문제는 "구간 합"만 필요하므로 합 세그트리로 구성
    # arr[idx] = 각 위치에 영화가 있는지의 여부
    # tree[node] = 이 노드 구간의 영화 개수 합
    st = SegmentTree[int, int](
        MAX_SIZE,
        identity=0,
        merge=lambda a, b: a + b,
        lift=lambda x: x,
        default=0,
    )

    update_set = st.update_set
    query = st.query

    out_lines = []

    for _ in range(t):
        n, m = map(int, input().split())
        movies = list(map(int, input().split()))

        # pos[x] = 영화 x가 현재 놓인 위치(0-based)
        pos = [0] * (n + 1)

        # top은 "다음에 영화를 올려둘 가장 위의 빈 자리"
        top = m - 1  # m - i

        # 초기 상태: 영화 1이 맨 위, 영화 n이 맨 아래
        # -> 영화 i를 위치 (m + i - 1)에 둔다.
        for i in range(1, n + 1):
            p = m + (i - 1)
            pos[i] = p
            update_set(p, 1)  # 그 위치에 영화가 있음을 표시 (st.arr[p] = 1)

        ans = []

        for x in movies:
            p = pos[x]

            # x의 "위에 있는 DVD 개수" = 구간 [0, p-1]의 합
            if p == 0:
                above = 0
            else:
                above = query(0, p - 1)
            ans.append(str(above))

            # 영화 x를 빼서(top으로 올리므로) 기존 위치는 비운다(0)
            update_set(p, 0)

            # 가장 위의 빈 자리(top)에 x를 올린다(1)
            update_set(top, 1)
            pos[x] = top
            top -= 1

        out_lines.append(" ".join(ans))

        # 현재 pos[1~n]에 값이 들어가 있는 상태
        for i in range(1, n + 1):
            update_set(pos[i], 0)

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()