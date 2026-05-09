class Graph:
    def __init__(self, adjacency_list):
        """
        Инициализация графа.

        :param adjacency_list (dict): Словарь вида
            вершина: множество соседних вершин
        Attributes:
        adjacency_list (dict): Словарь смежности графа.
        vertices (list): Список всех вершин графа.
        vertex_count (int): Количество вершин в графе.
        """
        self.adjacency_list = adjacency_list
        self.vertices = list(adjacency_list.keys())
        self.vertex_count = len(self.vertices)

    def is_independent(self, vertex_subset):
        """
        Проверяет, является ли множество вершин независимым.
        :param vertex_subset: Множество вершин для проверки.
        :return: bool: True, если множество независимое, иначе False.
        """
        for vertex_1 in vertex_subset:
            for vertex_2 in vertex_subset:
                if (
                    vertex_1 != vertex_2
                    and vertex_2 in self.adjacency_list[vertex_1]
                ):
                    return False
        return True

def maximal_sets(family):
    """
    Функция удаляет все множества, которые являются подмножествами других.
    """
    result_max = []

    for s in family:
        if not any(set(s) < set(t) for t in family):
            result_max.append(set(s))

    return result_max


def get_non_adjacent_vertices(graph, target_vertex, processed_vertices):
    """
    Функция ищет вершины, которые не соединены ребром с выбранной вершиной
    """
    return {
        vertex
        for vertex in processed_vertices
        if vertex != target_vertex
        and vertex not in graph.adjacency_list[target_vertex]
    }


# Алгоритм Беднарека–Толби
def bednarek_taulbee(graph):
    all_vertices = graph.vertices
    independent_family = [set()]

    for index in range(graph.vertex_count):
        current_vertex = all_vertices[index]
        updated_family = []

        for independent_set in independent_family:
            is_adjacent = any(
                current_vertex in graph.adjacency_list[v]
                for v in independent_set
            )

            if is_adjacent:
                updated_family.append(independent_set)

            else:
                updated_family.append(independent_set)

                extended_set = set(independent_set)
                extended_set.add(current_vertex)

                if graph.is_independent(extended_set):
                    updated_family.append(extended_set)

        independent_family = maximal_sets(updated_family)

        print(f"L{index + 1} =", independent_family)

    return independent_family

def main():
    graph_data = {
        "x1": {"x2", "x3", "x5"},
        "x2": {"x1", "x3"},
        "x3": {"x1", "x2", "x4", "x5"},
        "x4": {"x3"},
        "x5": {"x1", "x3"},
    }

    g = Graph(graph_data)

    result = bednarek_taulbee(g)

    print("\nНаибольшее Внутреннее Устойчивое Подмножество:")
    for s in result:
        print(s)


if __name__ == "__main__":
    main()
