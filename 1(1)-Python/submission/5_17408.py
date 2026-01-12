from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    # 구현하세요!
    """
    범용적인 세그먼트 트리(Segment Tree) 자료구조 클래스입니다.
    구간 합, 최소/최대값 쿼리 및 점 업데이트를 $O(\log N)$에 수행합니다.

    Attributes:
        - n (int): 원본 배열의 원소 개수.
        - identity (U): merge 연산의 항등원.
        - merge (Callable[[U, U], U]): 두 구간의 값을 결합하는 함수.
        - lift (Callable[[T], U]): 리프 노드의 값(T)을 트리 노드의 값(U)으로 변환하는 함수.
        - arr (list[T]): 현재 세그먼트 트리가 관리하는 원본 배열.
        - tree (list[U]): 트리의 노드들이 저장된 배열.

    Methods:
        - query: 지정된 구간의 요약 값을 반환합니다.
        - update_set: 특정 인덱스의 값을 새로운 값으로 교체합니다.
        - update_apply: 특정 인덱스의 값에 함수를 적용하여 갱신합니다.
        - find_kth: 누적합 등을 기준으로 k번째 원소의 인덱스를 탐색합니다.
    """

    def __init__(
        self,
        n: int,
        identity: U,
        merge: Callable[[U, U], U],
        lift: Callable[[T], U],
        default: T,
    ):
        """
        세그먼트 트리 초기화

        n        : 전체 원소 개수 (인덱스 범위: 0 ~ n-1)
        identity : merge 연산의 항등원 (합이면 0, 최소면 +inf 등)
        merge    : 두 구간 값을 합치는 함수
        lift     : 리프 값(T)을 노드 값(U)으로 변환하는 함수
        default  : 초기 배열에 채울 기본 리프 값
        """
        if n <= 0:
            raise ValueError("n은 양수여야 합니다.")

        self.n = n
        self.identity = identity
        self.merge = merge
        self.lift = lift

        # 리프에 해당하는 원본 배열 (point update 시 사용)
        self.arr: list[T] = [default for _ in range(n)]

        # 세그먼트 트리 배열 (4 * n이면 충분)
        self.tree: list[U] = [identity for _ in range(4 * n)]

        # 루트 노드(1번)부터 트리 빌드
        self._build(1, 0, n - 1)

    def _build(self, node: int, start: int, end: int) -> None:
        """
        세그먼트 트리 빌드 함수

        node  : 현재 노드 번호
        start : 이 노드가 담당하는 구간의 시작 인덱스
        end   : 이 노드가 담당하는 구간의 끝 인덱스
        """
        # 리프 노드인 경우
        if start == end:
            # 리프 값(T)을 노드 값(U)으로 변환해서 저장
            self.tree[node] = self.lift(self.arr[start])
            return

        mid = (start + end) // 2

        # 왼쪽 / 오른쪽 자식 빌드
        self._build(node * 2, start, mid)
        self._build(node * 2 + 1, mid + 1, end)

        # 현재 노드 값 = 왼쪽 + 오른쪽 구간 값
        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1],
        )

    # =========================
    # 구간 쿼리 (Range Query)
    # =========================
    def query(self, left: int, right: int) -> U:
        """
        구간 [left, right]의 요약 값을 반환
        """
        if not (0 <= left <= right < self.n):
            raise IndexError("쿼리 범위가 올바르지 않습니다.")
        return self._query(1, 0, self.n - 1, left, right)

    def _query(
        self,
        node: int,
        start: int,
        end: int,
        left: int,
        right: int,
    ) -> U:
        # 1. 전혀 겹치지 않는 경우
        if right < start or end < left:
            return self.identity

        # 2. 완전히 포함되는 경우
        if left <= start and end <= right:
            return self.tree[node]

        # 3. 일부만 겹치는 경우 → 자식으로 내려감
        mid = (start + end) // 2
        left_val = self._query(node * 2, start, mid, left, right)
        right_val = self._query(node * 2 + 1, mid + 1, end, left, right)

        return self.merge(left_val, right_val)

    # =========================
    # 점 업데이트 (Point Update)
    # =========================
    def update_set(self, idx: int, value: T) -> None:
        """
        arr[idx] 값을 value로 '설정'
        """
        if not (0 <= idx < self.n):
            raise IndexError("idx 범위 초과")
        self.arr[idx] = value
        self._update_set(1, 0, self.n - 1, idx)

    def _update_set(
        self,
        node: int,
        start: int,
        end: int,
        idx: int,
    ) -> None:
        # 리프 노드에 도달
        if start == end:
            self.tree[node] = self.lift(self.arr[idx])
            return

        mid = (start + end) // 2

        # idx가 속한 자식 노드로 이동
        if idx <= mid:
            self._update_set(node * 2, start, mid, idx)
        else:
            self._update_set(node * 2 + 1, mid + 1, end, idx)

        # 부모 노드 값 갱신
        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1],
        )

    def update_apply(self, idx: int, fn: Callable[[T], T]) -> None:
        """
        arr[idx]에 함수 fn을 적용한 뒤 트리를 갱신
        (예: 개수 +C / -C 같은 델타 업데이트)
        """
        if not (0 <= idx < self.n):
            raise IndexError("idx 범위 초과")
        self.arr[idx] = fn(self.arr[idx])
        self._update_set(1, 0, self.n - 1, idx)

    # =========================
    # 유틸리티
    # =========================
    def total(self) -> U:
        """
        전체 구간의 요약 값 반환
        """
        return self.tree[1]

    # =========================
    # k번째 원소 탐색 (Order Statistic)
    # =========================
    def find_kth(self, k: int) -> int:
        """
        누적합 기준으로 k번째 원소의 인덱스를 반환

        전제 조건:
        - U는 '개수/합'처럼 비교 가능한 값
        - 모든 값은 음이 아닌 값
        """
        if k <= 0:
            raise ValueError("k는 1 이상이어야 합니다.")
        if self.total() < k:  # type: ignore
            raise ValueError("k가 전체 개수보다 큽니다.")

        return self._find_kth(1, 0, self.n - 1, k)

    def _find_kth(
        self,
        node: int,
        start: int,
        end: int,
        k: int,
    ) -> int:
        # 리프 노드 도달 → 정답
        if start == end:
            return start

        mid = (start + end) // 2
        left_node = node * 2
        right_node = node * 2 + 1

        # 왼쪽 자식 구간의 합
        left_sum = self.tree[left_node]

        # k번째가 왼쪽에 있는지 판단
        if left_sum >= k:  # type: ignore
            return self._find_kth(left_node, start, mid, k)
        else:
            # 오른쪽으로 갈 경우 k에서 왼쪽 합을 빼줌
            return self._find_kth(
                right_node,
                mid + 1,
                end,
                k - left_sum,  # type: ignore
            )



import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # 구현하세요!
    pass


if __name__ == "__main__":
    main()