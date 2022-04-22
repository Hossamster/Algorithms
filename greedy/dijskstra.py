from math import inf 
src = 'A'
dest = 'F'
    
graph = {
    'A':{'B':2,'C':4},
    'B':{'A':2,'C':3,'D':8},
    'C':{'A':4,'B':3,'E':5,'D':2},
    'D':{'B':8,'C':2,'E':11,'F':22},
    'E':{'C':5,'D':11,'F':1},
    'F':{'D':22,'E':1}
}

nodes = {
    'A':{'cost':inf,'pre': None},
'B':{'cost':inf,'pre':None},
'C':{'cost':inf,'pre':None},
'D':{'cost':inf,'pre':None},
'E':{'cost':inf,'pre':None},
'F':{'cost':inf,'pre':None}
}
nodes[src]['cost'] = 0
temp = src
paths = []

for i,j in graph.items():
    for k in j:
        if graph[i].get(k) and i != src:
            if nodes[i]['cost'] > graph[i].get(k) + nodes[k]['cost']:
                nodes[i]['cost'] = graph[i].get(k) + nodes[k]['cost']
                nodes[i]['pre'] =  k
print(nodes)

"""{'A': {'cost': 0, 'pre': None}, 
'B': {'cost': 2, 'pre': 'A'}, 
'C': {'cost': 4, 'pre': 'A'}, 
'D': {'cost': 6, 'pre': 'C'}, 
'E': {'cost': 9, 'pre': 'C'}, 
'F': {'cost': 10, 'pre': 'E'}}"""

for i in nodes.keys():
    if nodes[i]['pre'] not in paths and i!= src:
        paths.append(nodes[i]['pre'])
paths.append(dest)
print(paths)