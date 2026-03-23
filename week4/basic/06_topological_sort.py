"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화 // adj = adjacency list(인접 리스트)
    graph = { vertice : [] for vertice in range(vertices)}
    in_degree = [0] * vertices
    
    # TODO: 그래프 구성 및 진입 차수 계산
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    queue = deque([i for i in range(vertices) if in_degree[i] == 0])
    result = []
    
    # TODO: 큐가 빌 때까지 반복
    while queue:
    ## 큐에서 정점 꺼내기
        current = queue.popleft()
        result.append(current)
    ## 인접한 정점들의 진입 차수 감소
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 사이클 체크
    # 모든 정점을 돌지 못했다면 사이클이 있는 상황
    if len(result) < vertices:
        return "Error: 사이클이 존재합니다"

    return result

'''
# 객체 지향적 코드 ## task_names
from collections import deque

class Task:
    """작업(과목) 하나하나를 나타내는 설계도"""
    def __init__(self, name):
        self.name = name
        self.links = []      # 다음에 할 작업들 (Adjacency List)
        self.in_degree = 0   # 나를 하기 위해 먼저 해야 할 일의 개수

def topological_sort(task_names, edges):
    # 1. 모든 작업 객체 생성 (딕셔너리에 담기)
    tasks = {name: Task(name) for name in task_names}
    
    # 2. 관계(간선) 연결 및 진입 차수 계산
    for u, v in edges:
        tasks[u].links.append(tasks[v])
        tasks[v].in_degree += 1
        
    # 3. 진입 차수가 0인(당장 시작 가능한) 작업 찾기
    queue = deque([t for t in tasks.values() if t.in_degree == 0])
    result = []
    
    # 4. 큐가 빌 때까지 반복 (Kahn's Algorithm)
    while queue:
        curr = queue.popleft()
        result.append(curr.name)
        
        for next_task in curr.links:
            next_task.in_degree -= 1
            if next_task.in_degree == 0:
                queue.append(next_task)
                
    # 5. 사이클 체크 (모든 작업을 다 못 했다면?)
    if len(result) < len(task_names):
        return None # 사이클 발생!
        
    return result

# --- 여기서부터 격리된 테스트 코드 ---
if __name__ == "__main__":
    # 데이터 준비
    subjects = ["기초", "중급", "응용", "고급"]
    relations = [
        ("기초", "중급"), 
        ("기초", "응용"), 
        ("중급", "고급"), 
        ("응용", "고급")
    ]
    
    print("🚀 위상 정렬 시뮬레이션 시작")
    order = topological_sort(subjects, relations)
    
    if order:
        print(f"✅ 추천 수강 순서: {' -> '.join(order)}")
    else:
        print("❌ 오류: 과목 관계에 사이클이 있어 순서를 정할 수 없습니다.")
'''

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
