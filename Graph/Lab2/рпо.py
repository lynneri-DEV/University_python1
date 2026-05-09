class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.vertices = list(adjacency_list.keys())
        self.vertex_count = len(self.vertices)

    def is_independent(self, vertex_subset):
        """Проверяет, является ли множество вершин независимым."""
        for v1 in vertex_subset:
            for v2 in vertex_subset:
                if v1 != v2 and v2 in self.adjacency_list[v1]:
                    return False
        return True

def maximal_sets(family):
    """Удаляет все множества, которые являются подмножествами других."""
    result_max = []
    for s in family:
        if not any(set(s) < set(t) for t in family):
            result_max.append(set(s))
    return result_max

# Алгоритм Беднарека–Толби с поиском наибольшего множества
def bednarek_taulbee_max(graph):
    all_vertices = graph.vertices
    independent_family = [set()]  # начинаем с пустого множества

    for index in range(graph.vertex_count):
        current_vertex = all_vertices[index]
        updated_family = []

        for indep_set in independent_family:
            # Проверка, можно ли добавить вершину
            if graph.is_independent(indep_set | {current_vertex}):
                extended_set = indep_set | {current_vertex}
                updated_family.append(extended_set)

            # Сохраняем текущее множество тоже
            updated_family.append(indep_set)

        # Оставляем только максимальные множества на данном шаге
        independent_family = maximal_sets(updated_family)

    # Теперь из максимальных выбираем наибольшее по размеру
    max_size = max(len(s) for s in independent_family)
    largest_sets = [s for s in independent_family if len(s) == max_size]

    return largest_sets

def main():
    graph_data = {
        "x1": {"x2", "x5"},
        "x2": {"x1", "x3"},
        "x3": {"x2", "x4"},
        "x4": {"x3", "x5"},
        "x5": {"x1", "x4"},
    }

    g = Graph(graph_data)

    result = bednarek_taulbee_max(g)

    print("Наибольшее Внутренне Устойчивое Подмножество:")
    for s in result:
        print(s)

if __name__ == "__main__":
    main()