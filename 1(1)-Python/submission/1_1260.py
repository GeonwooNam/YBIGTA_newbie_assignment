from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
그래프 탐색(DFS/BFS) 라이브러리 모듈.

- 정점 번호는 1 ~ n (1-based)로 가정합니다.
- 인접 행렬(adjacency matrix)을 사용합니다.
- 탐색 시, "번호가 작은 정점부터" 방문하도록 구현되어 있습니다.
"""


class Graph:
    """
    무방향 그래프를 표현하고 DFS/BFS 탐색을 지원하는 클래스입니다.

    Attributes:
        n (int): 정점의 개수 (정점 번호는 1 ~ n)
        graph (list[list[int]]): 인접 행렬. graph[u][v] == 1 이면 간선 존재.
    """
    def __init__(self, n: int) -> None:
        """
        그래프 초기화

        Args:
            n (int): 정점의 개수 (정점 번호는 1부터 n까지)
        """
        self.n = n
        # 구현하세요!
        self.graph = [[0 for _ in range(0, n+1)] for _ in range(0, n+1)]  # 인접 행렬

    
    def add_edge(self, u: int, v: int) -> None:
        """
        그래프에 양방향 간선 추가

        Args:
            u (int): 간선의 한쪽 정점 번호
            v (int): 간선의 다른쪽 정점 번호

        Notes:
            - 양방향 그래프이므로 (u, v), (v, u)를 모두 1로 설정합니다.
        """
        # 구현하세요!
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    
    def dfs(self, start: int) -> list[int]:
        """
        깊이 우선 탐색(DFS)

        Args:
            start (int): 탐색을 시작할 정점 번호

        Returns:
            list[int]: DFS 방문 순서

        Notes:
            - 스택(반복문) 방식으로 구현합니다.
            - "번호가 작은 정점부터" 방문되도록, 스택에는 큰 번호부터 push합니다.
              (LIFO 구조이므로 나중에 작은 번호가 먼저 pop됨)
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
        너비 우선 탐색(BFS)을 수행하고 방문 순서를 반환합니다.

        Args:
            start (int): 탐색을 시작할 정점 번호

        Returns:
            list[int]: BFS 방문 순서

        Notes:
            - 큐(Queue)를 사용합니다.
            - 인접 정점은 작은 번호부터 큐에 들어가도록 1부터 n까지 순회합니다.
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

        Args:
            start (int): 탐색을 시작할 정점 번호
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
