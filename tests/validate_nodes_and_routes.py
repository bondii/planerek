from scripts.node_operations import (
    plot_nodes,
    read_nodes_as_dataframe,
    read_all_nodes_from_csv,
)


from scripts.route_operations import plot_routes, read_all_routes_from_csv


def validate_nodes_and_maps():
    nodes = read_all_nodes_from_csv()
    routes = read_all_routes_from_csv()
    nodes_df = read_nodes_as_dataframe()

    fig, ax = plot_nodes(nodes)
    fig, ax = plot_routes(routes, nodes_df, fig, ax)

    fig.savefig("nodes_plot.jpg")
