import sys
from src.map_parser_pkg.scripts.odr_map_obj import opendrive


def check_driving_lanes(road):
    is_driving = False  # For selecting roads that have driving lanes also
    # Checking if left lanes have any driving lane
    if road.lanes.lanesection.left:
        if road.lanes.lanesection.left.lane_list:
            for lane in road.lanes.lanesection.left.lane_list:
                if lane.type == "driving":
                    is_driving = True
        else:
            if road.lanes.lanesection.left.lane.type == "driving":
                is_driving = True
    # Checking if center lanes have any driving lane
    if road.lanes.lanesection.center:
        if road.lanes.lanesection.center.lane.type == "driving":
            is_driving = True
    # Checking if right have any driving lane
    if road.lanes.lanesection.right:
        if road.lanes.lanesection.right.lane_list:
            for lane in road.lanes.lanesection.right.lane_list:
                if lane.type == "driving":
                    is_driving = True
        else:
            if road.lanes.lanesection.right.lane.type == "driving":
                is_driving = True
    # If is there any driving lane than add that road to the graph
    return is_driving


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def make_graph(self):
        init_graph = {}
        length = 0
        for roads in opendrive.road_Nonelist:
            if roads.link.successor.elementtype == "road":
                for road in opendrive.road_list:
                    if roads.link.successor.elementid == road.id:
                        if check_driving_lanes(roads) and check_driving_lanes(road):
                            length = float(road.length)
                            init_graph[roads] = {}
                            init_graph[roads.id][roads.link.successor.elementid] = length
                            # map_graph.append(list((roads.id, roads.link.successor.elementid, False)))
            elif roads.link.successor.elementtype == "junction":
                for junction in opendrive.junction_list:
                    if junction.id == roads.link.successor.elementid:
                        for connections in junction.connection_list:
                            if connections.incomingroad == roads.id:
                                for road in opendrive.road_list:
                                    if connections.connectingroad == road.id:
                                        if check_driving_lanes(roads) and check_driving_lanes(road):
                                            length = float(road.length)
                                            init_graph[roads] = {}
                                            init_graph[roads.id][connections.connectingroad] = length
                                            # map_graph.append(list((roads.id, connections.connectingroad, False)))
            if roads.link.predecessor.elementtype == "road":
                for road in opendrive.road_list:
                    if roads.link.predecessor.elementid == road.id:
                        if check_driving_lanes(roads) and check_driving_lanes(road):
                            length = float(road.length)
                            init_graph[roads] = {}
                            init_graph[roads.id][roads.link.predecessor.elementid] = length
                            # map_graph.append(list((roads.id, roads.link.predecessor.elementid, False)))
            elif roads.link.predecessor.elementtype == "junction":
                for junction in opendrive.junction_list:
                    if junction.id == roads.link.predecessor.elementid:
                        for connections in junction.connection_list:
                            if connections.incomingroad == roads.id:
                                for road in opendrive.road_list:
                                    if connections.connectingroad == road.id:
                                        if check_driving_lanes(roads) and check_driving_lanes(road):
                                            length = float(road.length)
                                            init_graph[roads] = {}
                                            init_graph[roads.id][connections.connectingroad] = length
                                            # map_graph.append(list((roads.id, connections.connectingroad, False)))

    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if not graph[adjacent_node].get(node, False):
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        roads = opendrive.road_list
        return roads

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False):
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]

    def dijkstra_algorithm(self, graph, start_node):
        unvisited_nodes = list(graph.get_nodes())
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize

        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
            unvisited_nodes.remove(current_min_node)
        return previous_nodes, shortest_path

    def print_result(self, previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
        path.append(start_node)

        print("shortest path ".format(shortest_path[target_node]))
        print(" -> ".join(reversed(path)))


def main():
    roads = opendrive.road_list

    graph = Graph(roads, "10")
    previous_nodes, shortest_path = graph.dijkstra_algorithm(graph=graph, start_node="0")
    graph.print_result(previous_nodes, shortest_path, start_node="0", target_node="3")


if __name__ == "main":
    main()

