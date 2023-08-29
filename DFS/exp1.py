#!/usr/bin/python3
# -*-coding:utf-8-*-
# from:https://hiyongz.github.io/posts/algorithm-notes-for-dfs-bfs/

#  图的DFS遍历
from collections import defaultdict


class Graph:
    def __init__(self):
        # 使用字典保存图
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        # 用于给图添加边（连接）
        self.graph[u].append(v)

    def DFSTrav(self, v, visited):
        # 标记已经访问过的节点
        visited.append(v)

        # 访问当前节点的相邻节点
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSTrav(neighbour, visited)

    def DFS(self, v):
        # 初始化保存已访问节点的集合
        visited = []

        # 递归遍历节点
        self.DFSTrav(v, visited)
        print(visited)

    def DFS2(self, v):
        visited = []
        stack = []
        stack.append(v)
        visited.append(v)
        while stack:
            for i in self.graph[v]:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)
                    break
            v = stack[-1]
            if set(self.graph[v]) < set(visited):
                stack.pop(-1)
        print(visited)
    def BFS(self, v):
        queue = []
        queue.append(v)
        visited = []
        visited.append(v)
        while queue:
            v = queue.pop(-1)
            for i in self.graph[v]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        print(visited)


if __name__ == "__main__":
    # 新建图
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 0)
    graph.addEdge(2, 0)
    graph.addEdge(3, 0)
    graph.addEdge(1, 4)
    graph.addEdge(2, 4)
    graph.addEdge(3, 2)
    graph.addEdge(4, 1)
    graph.addEdge(4, 2)
    graph.addEdge(4, 3)

    # DFS遍历图：指定一个起点
    graph.DFS(0)
    graph.DFS2(0)
    graph.BFS(0)
