
def read_max_flow_graph(filepath):
    """Lit un fichier .txt pour un problème de flot maximum."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        capacity_matrix = []
        for line in lines[1:n+1]:
            row = list(map(int, line.strip().split()))
            capacity_matrix.append(row)
    return n, capacity_matrix


def read_min_cost_flow_graph(filepath):
    """Lit un fichier .txt contenant deux matrices : capacité et coût."""
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    capacity_matrix = []
    cost_matrix = []

    try:
        capacity_start = lines.index("CAPACITY") + 1
        cost_start = lines.index("COST") + 1
    except ValueError:
        raise ValueError("Fichier mal formaté : il faut les balises 'CAPACITY' et 'COST'.")

    for i in range(capacity_start, capacity_start + n):
        capacity_matrix.append(list(map(int, lines[i].split())))

    for i in range(cost_start, cost_start + n):
        cost_matrix.append(list(map(int, lines[i].split())))

    return n, capacity_matrix, cost_matrix


def display_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    n = len(matrix)
    print("    " + " ".join(f"{j+1:>4}" for j in range(n)))
    print("    " + "-" * (5 * n))
    for i in range(n):
        row_str = " ".join(f"{matrix[i][j]:>4}" for j in range(n))
        print(f"{i+1:>2} | {row_str}")
