def IsNegativeWeightCyclePresent(WList):
    rows = len(WList.keys())
    infinity = len(WList.keys()) * max([d for u in WList.keys() for (v, d) in WList[u]]) + 1
    distance = {}
    prev_dist = {}
    for v in WList.keys():
        distance[v], prev_dist[v] = infinity, infinity
    distance[0] = 0
    for i in range(len(WList.keys()) + 1):
        for u in WList.keys():
            prev_dist[u] = distance[u]
        for u in WList.keys():
            for (v, d) in WList[u]:
                distance[v] = min(distance[v], distance[u] + d)
    for v in distance.keys():
        if distance[v] < prev_dist[v]:
            return True
    return False
