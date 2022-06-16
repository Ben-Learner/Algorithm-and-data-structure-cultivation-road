states_needed = set(['a','b','c','d','e','f','g']) #创建集合
stations = {}
stations['s1'] = set(['a','b','g'])
stations['s2'] = set(['b','g','e','f'])
stations['s3'] = set(['c','b','e','a'])
stations['s4'] = set(['c','d','b','f'])
# print(stations)
final_stations = set()
# for station, states in station.items():
#     print(states)
while states_needed:
    best_station = None
    states_coverd = set()
    for station,states in stations.items():
        coverd = states_needed & states
        if len(coverd) > len(states_coverd):
            states_coverd = coverd
            best_station = station
    states_needed -= states_coverd
    final_stations.add(best_station)
print(final_stations)
