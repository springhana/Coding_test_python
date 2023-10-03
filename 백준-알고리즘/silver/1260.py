from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)

# 노드 표시
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(start):
    visited_dfs[start] = 1
    print(start, end=' ')
    for i in range(1, n + 1):
        if visited_dfs[i] == 0 and graph[start][i] == 1:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited_bfs[start] = 1
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(1, n + 1):
            if visited_bfs[i] == 0 and graph[node][i] == 1:
                queue.append(i)
                visited_bfs[i] = 1


dfs(v)
print()
bfs(v)
