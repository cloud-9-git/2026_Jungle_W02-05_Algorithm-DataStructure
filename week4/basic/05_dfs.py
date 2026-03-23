"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO: visited가 None이면 초기화
    if visited == None:
        visited = []
    
    # TODO: 현재 정점 방문
    visited.append(start)
    
    # TODO: 인접한 정점들에 대해 재귀
    ## 방문하지 않은 정점이면 재귀 호출
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited


def dfs2(graph, start, visited=None):
    """
    깊이 우선 탐색 (# while과 stack을 사용하여 구현하는 방식)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    if visited is None:
        visited = []
    
    visited_check = set()
    stack = [start]  # 시작 노드를 스택에 넣고 시작
    
    while stack:
        current = stack.pop()  # 가장 최근에 넣은 노드를 꺼냄 (LIFO)
        
        if current not in visited_check:
            visited_check.add(current)  # 방문 체크 (add 사용!)
            visited.append(current)     # 방문 순서 기록
            
            # 현재 노드와 연결된 인접 노드들을 스택에 추가
            # 역순으로 넣으면 숫자가 작은 노드부터 방문하게 됩니다.
            for neighbor in reversed(graph[current]):
                if neighbor not in visited_check:
                    stack.append(neighbor)
    
    return visited


# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


