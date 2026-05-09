# Лабораторная работа №1
## Тема: Алгоритмы для нахождения Наибольшего Внутренне Устойчивого Подмножества. Алгоритм Беднарека и Толби.
**Дисциплина:** Дискретная математика  
**Студенты:** Севастьянов Артём / Петровская Арина 
**Группа:** IA2504  
**Преподаватель:** Цуркану К.  
**Год:** 2026  

---

### Выполнение лабораторной работы
```python
class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.vertices = list(adjacency_list.keys())
        self.vertex_count = len(self.vertices)

    def is_independent(self, vertex_subset):
        for vertex_1 in vertex_subset:
            for vertex_2 in vertex_subset:
                if (
                    vertex_1 != vertex_2
                    and vertex_2 in self.adjacency_list[vertex_1]
                ):
                    return False
        return True
```  
Переменные:  
- `adjacency_list` граф в виде словаря, где ключ — вершина, а значение — множество соседних вершин(принимается от пользователя).
- `vertices` хранит список всех вершин графа.
- `vertex_count` счетчик для количества вершин в графе  

Метод `is_independent` 
- `vertex_subset` множество вершин, которое мы хотим проверить на независимость.
- `vertex_1` и `vertex_2` из множества `vertex_subset`.

Функция перебирает все пары вершин из переданного множества и проверяет, соединены ли они ребром. 
Если находятся две разные вершины, которые являются соседями в графе, функция сразу возвращает `False`, 
то есть множество не является независимым. Если ни одна пара вершин не соединена ребром, функция возвращает `True`, 
значит множество независимое.

```python
def maximal_sets(family):
    result_max = []

    for s in family:
        if not any(set(s) < set(t) for t in family):
            result_max.append(set(s))

    return result_max
```  
- `family` список множеств вершин.
- `result_max` пустой список, для максимальных множеств  

Функция `maximal_sets` получает список множеств вершин и оставляет в нём только максимальные множества. Она по очереди 
берёт каждое множество `s` и проверяет, существует ли в этом же списке другое множество `t`, которое строго больше него, то 
есть полностью содержит `s`. Для этого используется проверка `set(s) < set(t)`. Если такое множество находится, значит `s` 
можно расширить и оно не является максимальным, поэтому оно отбрасывается. Если же ни одного большего множества не 
найдено, то `s` считается максимальным и добавляется в результирующий список `result_max`. После проверки всех множеств 
функция возвращает список только максимальных множеств.  
```python
def get_non_adjacent_vertices(graph, target_vertex, processed_vertices):
    return {
        vertex
        for vertex in processed_vertices
        if vertex != target_vertex
        and vertex not in graph.adjacency_list[target_vertex]
    }
```  
- `graph` объект класса Graph.
- `target_vertex` вершина, относительно которой идёт проверка.
- `processed_vertices` множество уже обработанных вершин.
- `vertex` текущая вершина из перебора.  
Проверяем, не является ли вершина соседом `target_vertex`, если вершины соединены ребром — она НЕ подходит.  
```python
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
```
- `all_vertices` список всех вершин.
- `independent_family` текущее семейство независимых множеств.
- `current_vertex` вершина, которую сейчас пытаемся добавить в множества.
- `updated_family` новое семейство множеств, которое строится на текущем шаге.
- `is_adjacent` проверяем смежна ли новая вершина хотя бы с одной вершиной множества, `True` - добавить нельзя, `False` - можно попробовать расширить множество.
- `extended_set` копия текущего множества. Создаётся, чтобы не менять исходное множество.











