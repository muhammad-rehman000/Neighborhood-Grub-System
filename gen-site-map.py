import json

import pydot

edges = (
    ("home", "login"),
    ("home", "logout"),
    ("home", "dish posts"),
    ("home", "dish requests"),
    ("home", "account"),
    ("home", "suggestion"),
    ("login", "signup"),
    ("login", "home"),
    ("dish posts", "post detail"),
    ("dish posts", "orders"),
    ("dish requests", "request detail"),
    ("dish requests", "create request"),
    ("post detail", "chef profile"),
    ("orders", "cancel order"),
    ("orders", "create request"),
    ("account", "orders"),
    ("create request", "orders"),
)

def main():

    graph = pydot.Dot(graph_type="digraph")

    for u, v in edges:
        edge = pydot.Edge(u, v)
        graph.add_edge(edge)
    else:
        graph.write_png("site-map.png")

if __name__ == "__main__":
    main()
