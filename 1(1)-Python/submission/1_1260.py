from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ 구현하기
- add_edge 구현하기
- dfs 구현하기 (재귀 또는 스택 방식 선택)
- bfs 구현하기
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        그래프 초기화
        n: 정점의 개수 (1번부터 n번까지)
        """
        self.n = n
        # 구현하세요!
        self.graph = [[0 for _ in range(0, n+1)] for _ in range(0, n+1)]  # 인접 행렬

    
    def add_edge(self, u: int, v: int) -> None:
        """
        양방향 간선 추가
        """
        # 구현하세요!
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    
    def dfs(self, start: int) -> list[int]:
        """
        깊이 우선 탐색 (DFS)
        
        구현 방법 선택:
        1. 재귀 방식: 함수 내부에서 재귀 함수 정의하여 구현
        2. 스택 방식: 명시적 스택을 사용하여 반복문으로 구현
        """
        # 구현하세요!
        dfs_list = []  # DFS 탐색 결과
        visited = set()  # 방문 여부

        stack: deque[int] = deque()  # 스택 정의
        stack.append(start)

        while len(stack) > 0:
            # 스택에서 pop
            value = stack.pop()
            if value in visited:
                continue

            dfs_list.append(value)
            visited.add(value)

            # 인접 노드 추가
            for i in range(self.n, 0, -1):
                if self.graph[value][i] == 1:
                    stack.append(i)

        return dfs_list
    
    def bfs(self, start: int) -> list[int]:
        """
        너비 우선 탐색 (BFS)
        큐를 사용하여 구현
        """
        # 구현하세요!
        bfs_list = []  # DFS 탐색 결과
        visited = set()  # 방문 여부

        queue: deque[int] = deque()  # 큐 정의
        queue.append(start)
        visited.add(start)

        while len(queue) > 0:
            # 큐에서 pop
            value = queue.popleft()
            bfs_list.append(value)

            # 인접 노드 추가
            for i in range(1, self.n+1):
                if (self.graph[value][i] == 1) and (i not in visited):
                    queue.append(i)
                    visited.add(i)

        return bfs_list
    
    def search_and_print(self, start: int) -> None:
        """
        DFS와 BFS 결과를 출력
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))



from typing import Callable
import sys


"""
-아무것도 수정하지 마세요!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, M, V = intify(lines[0])
    
    graph = Graph(N)  # 그래프 생성
    
    for i in range(1, M + 1): # 간선 정보 입력
        u, v = intify(lines[i])
        graph.add_edge(u, v)
    
    graph.search_and_print(V) # DFS와 BFS 수행 및 출력


if __name__ == "__main__":
    main()
