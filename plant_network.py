import csv
import networkx as nx
from networkx.readwrite import json_graph
import json
import os.path
import flask


def getEdges(filename):
    with open(filename, 'r') as nodecsv:
        nodereader = csv.reader(nodecsv)
        edges = [tuple(e[2:]) for e in nodereader][1:]
        return edges


def getAggregatedEdgesAndRoles(edges):
    dic = {}
    roles = set()
    for x in edges:
        if (x[0], x[1]) in dic.keys():
            dic[(x[0], x[1])] = int(x[2]) + int(dic[(x[0], x[1])])
        else:
            dic[(x[0], x[1])] = int(x[2])
        roles.add(x[0])
        roles.add(x[1])
    aggregatedEdges = []
    for k, v in dic.items():
        aggregatedEdges.append((k[0], k[1], v))
    return aggregatedEdges , roles


current_dir = '.'
files = {
    'region_1_old':'region_1_old.csv',
    'region_2_old':'region_2_old.csv',
    'region_3_old':'region_3_old.csv',
    'region_4_old':'region_4_old.csv',
    'region_1_new':'region_1_new.csv',
    'region_2_new':'region_2_new.csv',
    'region_3_new':'region_3_new.csv',
    'region_4_new':'region_4_new.csv'

}

region_edges = {}
class_dict = {}

roles_set = set()
for k, v in files.items():
    region_file_name = k + '_edges'
    file_name = os.path.join(current_dir, v)
    edges = getEdges(file_name)
    aggregatedEdges, roles = getAggregatedEdgesAndRoles(edges)
    region_edges[region_file_name] = aggregatedEdges
    roles_set |= roles

supervisor_roles = ['shift_manager', 'supervisor_unspec', 'supervisors', 'control_room_sup']
engineering_roles = ['engineers_unspec', 'engineer_unspec']
control_op_roles = ['control_room_op', 'operator_unspec', 'operators_unspec']
undefined_tech_roles = ['tech_unspec']

for role in roles_set:
    if role in supervisor_roles:
        class_dict[role] = 1
    elif role in engineering_roles:
        class_dict[role] = 2
    elif role in control_op_roles:
        class_dict[role] = 3
    elif role in undefined_tech_roles:
        class_dict[role] = 4
    else:
        class_dict[role] = 0

graphs = {}
i = 0
for k, v in region_edges.items():
    k = k.replace('_edges', '')

    graph = nx.Graph()
    graph.add_nodes_from(roles_set)
    graph.add_weighted_edges_from(v)
    bet_dict = dict(nx.betweenness_centrality(graph))
    bet_dict.update((k, v*1000) for k, v in bet_dict.items())
    nx.set_node_attributes(graph, bet_dict, 'betweenness')
    nx.set_node_attributes(graph, class_dict, 'class')
    graphs[k] = graph

for graph, graphdata in graphs.items():
    filename = 'force/'+graph+'.json'
    jsondata = json_graph.node_link_data(graphdata)
    json.dump(jsondata, open(filename, 'w'))
    # Wrote node-link JSON data to json file

app = flask.Flask(__name__, static_folder="force")


@app.route('/')
def static_proxy():
    return app.send_static_file('force.html')


print('\nGo to http://localhost:8000 to see the Visualization \n')
app.run(port=8000)
