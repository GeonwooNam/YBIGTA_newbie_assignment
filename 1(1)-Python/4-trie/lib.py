from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        current_idx = 0  # root

        for x in seq:
            is_in_children = False

            # x가 children에 존재하는 경우(주석 개선 필요)
            if self[current_idx].children:
                last_child_idx = self[current_idx].children[-1]
                if self[last_child_idx].body == x:
                    current_idx = last_child_idx
                    continue

            # x가 children에 존재하지 않는 경우
            if not is_in_children:
                insert_idx = len(self)
                self[current_idx].children.append(insert_idx)
                self.append(TrieNode(body=x))
                current_idx = insert_idx

        self[current_idx].is_end = True

    # 구현하세요!
    def count_orders(self, fact: list[int]) -> int:
        """
        전체 Trie 구조 내에서 가능한 유효한 순서의 개수를 계산합니다.
        팩토리얼 테이블을 사용하여 조합론적 경우의 수를 구합니다.

        Args:
            - fact (list[int]): 미리 계산된 팩토리얼 값들이 담긴 리스트.

        Returns:
            - total_count (int): 계산된 경우의 수 (Modulo 1,000,000,007).
        """
        return self._dfs(0, fact)

    def _dfs(self, u: int, fact: list[int]) -> int:
        """
        깊이 우선 탐색(DFS)을 통해 각 서브트리의 경우의 수를 재귀적으로 계산합니다.

        Args:
            - u (int): 현재 탐색 중인 노드의 인덱스.
            - fact (list[int]): 팩토리얼 테이블.

        Returns:
            - sub_res (int): 현재 노드를 루트로 하는 서브트리의 경우의 수.
        """
        res = 1
        blocks = 0
        mod = 1_000_000_007

        # 자식 서브트리들
        for v in self[u].children:
            res = (res * self._dfs(v, fact)) % mod
            blocks += 1

        # 이 노드에서 단어가 끝난다면 하나의 덩어리 추가
        if self[u].is_end:
            blocks += 1

        # 미리 계산된 팩토리얼 테이블 참조
        res = (res * fact[blocks]) % mod

        return res
