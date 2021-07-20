"""
Develop a data type with a Pythonic API suitable for representing graphs
that are directed and/or undirected, weighted and/or unweighted.
Make strategic use of Python's built-in types, OOP features, and standard
library to accomplish the above goal.
"""
__author__ = 'Yukio Rivera, ysrivera@jeff.cis.cabrillo.edu'

from collections import defaultdict, deque


class _Edges(dict):

  'Edge initializer'
  def __missing__(self, vertex):
    self.setdefault(vertex, True)

  def __delitem__(self, dst):
    self[dst] = False

  def del_vertex(self, dst):
    super().__delitem__(dst)

  def copy(self):
    y = _Edges()
    for k, v in self.items():
      y[k] = v
    return y


class Graph(defaultdict):

  "Graph Init"
  def __init__(self):
    super().__init__(_Edges)

  def __delitem__(self, vertex):
    rest = list(self[vertex])
    for orphans in rest:
      self[orphans]
    super().__delitem__(vertex)
    for k, v in self.items():
      if vertex in v:
        self[k].del_vertex(vertex)

  def __len__(self):
    if super().__len__() == 0:
      return 0
    else:
      return len(self.vertices())

  def copy(self):
    x = Graph()
    for k, v in self.items():
      x[k] = v.copy()
    return x

  def vertices(self):
    all_vert = set()
    for vertices in self.keys():
      all_vert.add(vertices)
      for othervertices in self[vertices].keys():
        all_vert.add(othervertices)
    return all_vert

  def edges(self):
    edge = {}
    all_edges = set()
    for source, destnweight in self.items():
      for key, value in destnweight.items():
        edge = (source, key, value)
        all_edges.add(edge)
    return all_edges

  def adjacent(self, src, dst):
    if src in self:
      if dst in self[src]:
        if self[src][dst]:
          return True
    return False

  def neighbors(self, vertex):
    barrio = set()
    for vert in self.vertices():
      if self.adjacent(vertex, vert):
        barrio.add(vert)
    return barrio

  def degree(self, vertex):
    return len(self.neighbors(vertex))

  def path_valid(self, vertices):
    if not self.path_length(vertices):
      return False
    else:
      return True

  def path_length(self, vertices):
    path = []
    for i in range(len(vertices) - 1):
      if not self.adjacent(vertices[i], vertices[i + 1]):
        return None
      else:
        path.append(self[vertices[i]][vertices[i + 1]])
    if not path:
      return None
    s = path[0]
    for i in range(1, len(path)):
      s += path[i]
    return s

  def is_connected(self):
    f_node = [self.keys()][0]
    que = deque(f_node)
    visited = set()
    while que:
      pops = que.popleft()
      check = self.neighbors(pops)
      for i in check:
        if i not in visited:
          visited.add(i)
          que.append(i)
    return self.vertices() == visited
