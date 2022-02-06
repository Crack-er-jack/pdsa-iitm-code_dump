def get_path(parent, v, path):
    if parent[v] == -1:
        path.append(v)
        return
    path.append(v)
    get_path(parent, parent[v], path)
def min_cost_walk(WL, S, D, V):
    # S to V
    visited1 = {}
    distance1 = {}
    parent1 = {}
    infinity = len(WL.keys()) * max([d for u in WL.keys() for (v, d) in WL[u]]) + 1
    for v in WL.keys():
        visited1[v], distance1[v], parent1[v] = False, infinity, -1
    distance1[S] = 0
    for u in WL.keys():
        nextd = min(distance1[v] for v in WL.keys() if not visited1[v])
        nextvList = [v for v in WL.keys() if not visited1[v] and distance1[v] == nextd]
        if nextvList == []:
            break
        nextv = min(nextvList)
        visited1[nextv] = True
        if visited1[V]:
            break
        for (v, d) in WL[nextv]:
            if not visited1[v]:
                prevd = distance1[v]
                distance1[v] = min(distance1[v], distance1[nextv] + d)
                if (distance1[v] != prevd):
                    parent1[v] = nextv
    walk_route1 = []
    get_path(parent1, V, walk_route1)
    # V to D
    visited2 = {}
    distance2 = {}
    parent2 = {}
    for v in WL.keys():
        visited2[v], distance2[v], parent2[v] = False, infinity, -1
    distance2[V] = 0
    for u in WL.keys():
        nextd = min(distance2[v] for v in WL.keys() if not visited2[v])
        nextvList = [v for v in WL.keys() if not visited2[v] and distance2[v] == nextd]
        if nextvList == []:
            break
        nextv = min(nextvList)
        visited2[nextv] = True
        if visited2[D]:
            break
        for (v, d) in WL[nextv]:
            if not visited2[v]:
                prevd = distance2[v]
                distance2[v] = min(distance2[v], distance2[nextv] + d)
                if (distance2[v] != prevd):
                    parent2[v] = nextv
    walk_route2 = []
    get_path(parent2, D, walk_route2)
    return (distance1[V] + distance2[D], walk_route1[::-1] + walk_route2[::-1][1:])
