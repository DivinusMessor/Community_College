__author__ = "Yukio Rivera"

import sys
import math
from collections import defaultdict
import pprint
import heapq

# Makes the map 
color_list = defaultdict(set)
info = []
counter = 0
with open("/srv/datasets/london_underground/routes.tsv", 'r') as colors:
  for n in colors:
    if counter != 0:
      src, dst, line = [int(i) for i in n.rstrip().split('\t')]
      color_list[src].add((dst, line))
      color_list[dst].add((src, line))
    counter += 1

# Prints the line number and the name. Will use for print output
name_line = {}
with open("/srv/datasets/london_underground/lines.tsv", 'r') as colors:
  counter = 0
  for n in colors:
    if counter != 0:
      line, name, colour = [i for i in n.rstrip().split('\t')[:3]]
      name_line[int(line)] = name
    counter += 1


# Print the line number and coordinates 
id_dict = dict()
# Prints the station name and number
st_name = dict()
# backwards number: station
num_st = dict()
with open("/srv/datasets/london_underground/stations.tsv", 'r') as stations:
  counter = 0
  for info in stations:
    if counter != 0:
      id, lat, long, name = [i for i in info.rstrip().split('\t')]
      id_dict[int(id)] = (float(long), float(lat))
      st_name[name] = int(id)
      num_st[int(id)] = name
    counter += 1

# Gets the user input for start, end, and penalty
srt = sys.argv[1]
end = sys.argv[2]
pen = float(sys.argv[3])


# Gets the number connected to the color
srt = st_name[srt]
end = st_name[end]


# great circle distance
def great_circle(coor2, coor1):
  lon1, lat1 = id_dict[coor1]
  lon2, lat2 = id_dict[coor2]
  tlon, tlat = lon2 - lon1, lat2 - lat1
  return 2 * math.asin(
      math.sqrt(
        math.sin(tlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(tlon / 2) ** 2)) * 6371

def dijkstras(srt, end):
  parent_node = {srt: None}
  Dist = {k : math.inf for k in id_dict}
  Dist[srt] = 0
  que = []
  heapq.heappush(que, (0, srt, None))
  while que:
    length, node, linee = heapq.heappop(que)
    # This will print all the neighbors of the node(srt) color_list.neighbors(node)
    for station in color_list[node]:
      new_distance = length + great_circle(node, station[0])
      if linee is not None and linee != station[1]:
        new_distance += pen
      #print(new_distance)
      if new_distance < Dist[station[0]]:
        Dist[station[0]] = new_distance
        parent_node[station[0]] = (node, station[1])
        heapq.heappush(que, (new_distance,station[0], station[1])) 
  return parent_node
test = dijkstras(srt, end)

def p_name(in_keys, s_key):
  cp = in_keys
  cp2 = s_key
  print(f'{num_st[cp[0]]} toward {num_st[cp2[0]]} using line{cp[1]}')
  if test[cp[0]] is not None:
    p_name(test[in_keys[0]], test[cp2[0]])
p_name(test[end],(end,None))
