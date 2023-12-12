class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.check_out = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.check_in[id]
        station_name = start_station[0]
        station_time = start_station[1]

        self.check_out[station_name].append((stationName, t - station_time))
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time = 0
        count = 0

        for end_station in self.check_out[startStation]:
            end_station_name = end_station[0]
            time_taken = end_station[1]
            if end_station_name == endStation:
                total_time += time_taken
                count += 1
        
        return total_time / count if count != 0 else -1
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

"""
Solution: graph
1. store the customer checkin in dictionary
2. checkout - retrive the intional position #1 and build the graph 
3. getave - itrate over the graph starting from statstat nodes which are endstation


in = {45 : "le, 3", 32 : "pa, 8","27" : "le, 10", "10" : "le, 24"}

ou = {"le" : ["wa, 12", "wo, 10", "wa, 14"]
        "pa" : ["ca, 14"]}


Complexty:
TC: CHECKIN - O(1)
    CHECKOUT - O(1)
    GETAVE - O(N) - N-NUMBER OF STATIONS

SC: CHECIN - O(S) - S - START STATIONS
    CHECOUT - O(S * E) - 100



"""