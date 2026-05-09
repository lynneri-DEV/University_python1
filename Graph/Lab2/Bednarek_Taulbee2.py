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
    Оставляет только максимальные по включению множества[cite: 17, 23].
    """
    if not family:
        return []

    # Превращаем элементы в замороженные множества для корректного сравнения
    unique_sets = []
    for s in family:
        fs = set(s)
        if fs not in unique_sets:
            unique_sets.append(fs)

    result_max = []
    for s in unique_sets:
        # Если s не является подмножеством никакого другого множества t в семействе
        if not any((s < t) for t in unique_sets):
            if s not in result_max:
                result_max.append(s)

    return result_max


def get_non_adjacent_vertices(graph, target_vertex, processed_vertices):
    """
    Функция ищет вершины из уже обработанных (X_k), которые не соединены ребром
    с выбранной вершиной (x_{k+1}), включая саму целевую вершину[cite: 6, 11].
    """
    non_adj = {
        vertex
        for vertex in processed_vertices
        if vertex not in graph.adjacency_list[target_vertex]
    }
    non_adj.add(target_vertex)
    return non_adj


# Алгоритм Беднарека–Толби
def bednarek_taulbee(graph):
    """
    Реализация алгоритма Беднарека-Толби.
    Находит все максимальные внутренне устойчивые подмножества.
    """
    all_vertices = graph.vertices
    if not all_vertices:
        return []   # берем список всех вершин графа, если граф пуст, возвращаем пустоту.

    current_x_k = [all_vertices[0]]
    independent_family = [{all_vertices[0]}]  # L1

    print(f"L1 = {independent_family}")

    for k in range(1, graph.vertex_count):
        # вершина, которую мы пытаемся встроить в уже найденные независимые группы на текущем шаге
        xk_plus_1 = all_vertices[k] # перебираем вершины графа по одной (вторую, третью и т.д.)

        yk_plus_1 = get_non_adjacent_vertices(graph, xk_plus_1, current_x_k) # смотрим на все вершины, которые
        # уже были обработаны (current_x_k), и выбираем среди них те, которые НЕ соединены ребром с нашей новой вершиной xk_plus_1

        ik_star = [] # оставляем только самые большие из этих пересечений, удаляя те, которые являются частью других
        for m in independent_family:
            ik_star.append(m.intersection(yk_plus_1))

        ik = maximal_sets(ik_star)

        lk_plus_1_star = []
        for m in independent_family:
            if m.issubset(yk_plus_1): # Если новая вершина не соединена ни с кем из группы m, мы просто добавляем её в эту группу.
                lk_plus_1_star.append(m.union({xk_plus_1}))
            else:
                lk_plus_1_star.append(m)
                intersection = m.intersection(yk_plus_1)
                if intersection in ik:
                    lk_plus_1_star.append(intersection.union({xk_plus_1}))

        independent_family = maximal_sets(lk_plus_1_star)

        current_x_k.append(xk_plus_1)

        print(f"L{k + 1} = {independent_family}")

    return independent_family


def main():
    # Пример графа
    graph_data = {
        "x1": {"x2", "x5"},
        "x2": {"x1", "x3"},
        "x3": {"x2", "x4"},
        "x4": {"x3", "x5"},
        "x5": {"x1", "x4"},
    }

    g = Graph(graph_data)

    result = bednarek_taulbee(g)

    # Поиск НВУП (наибольшего по размеру) [cite: 40-41]
    print("\nМаксимальные независимые множества:")
    max_size = 0
    for s in result:
        print(s)
        if len(s) > max_size:
            max_size = len(s)

    print(f"\nЧисло внутренней устойчивости α0(G) = {max_size}")
    print("Наибольшие Внутренне Устойчивые Подмножества:")
    for s in result:
        if len(s) == max_size:
            print(s)


if __name__ == "__main__":
    main()
