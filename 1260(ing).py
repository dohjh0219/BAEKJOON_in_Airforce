# 1260 DFS와 BFS

import sys

n,m,v = map(int,sys.stdin.readline().split())

graph=dict()
for i in range(1,n+1):
    graph[i]=list()

for _ in range(m):
    node1, node2 = map(int,sys.stdin.readline().split())
    graph[node1].append(node2)

def dfs(graph, start_node):
    # 방문해야 할 노드와 방문한 노드를 두 개의 별도의 리스트로 관리함.
    need_visited = list()
    visited=list()
    
    need_visited.append(start_node) # 초기 시작 노드를 방문해야 할 노드 리스트에 추가.
    
    while len(need_visited)!=0: # 방문해야 할 노드가 필요하다면,
        node=need_visited.pop()  # 그 중 마지막 데이터 추출(스택 구조(후입선출)이용)
        
        if node not in visited: # 해당 노드가 방문 목록에 없다면,
            visited.append(node) # 방문 목록에 추가.
            need_visited.extend(graph[node])  #extend는 추가하려는 리스트의 내용 전부를 내용만 추가함.
            
    return visited

print(dfs(graph,v))