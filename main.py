from utils.graph_io import read_max_flow_graph, read_min_cost_flow_graph, display_matrix

def test_maxflow():
    print("=== Test Max Flow: proposal1.txt ===")
    try:
        n, capacity = read_max_flow_graph("data/proposal1.txt")
        print(f"Graph with {n} nodes")
        display_matrix(capacity, title="Capacity Matrix")
    except Exception as e:
        print("Erreur lors de la lecture de proposal1.txt :", e)

def test_mincost():
    print("\n=== Test Min Cost Flow: proposal6.txt ===")
    try:
        n, capacity, cost = read_min_cost_flow_graph("data/proposal6.txt")
        print(f"Graph with {n} nodes")
        display_matrix(capacity, title="Capacity Matrix")
        display_matrix(cost, title="Cost Matrix")
    except Exception as e:
        print("Erreur lors de la lecture de proposal6.txt :", e)

def main():
    test_maxflow()
    test_mincost()

if __name__ == "__main__":
    main()
