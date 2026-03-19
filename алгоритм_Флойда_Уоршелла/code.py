INF = 10**9  # бесконечность

def floyd_warshall(graph):
    """
    graph - квадратная матрица весов (list of lists)
    Возвращает:
        dist - матрица кратчайших расстояний,
        has_negative_cycle - флаг наличия отрицательного цикла
    """
    v = len(graph)
    dist = [row[:] for row in graph]

    # Основной цикл алгоритма
    for k in range(v):
        for i in range(v):
            if dist[i][k] == INF:
                continue
            for j in range(v):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    has_negative_cycle = any(dist[i][i] < 0 for i in range(v))

    return dist, has_negative_cycle


def print_matrix(matrix):
    """Красивый вывод матрицы."""
    v = len(matrix)
    print("    ", end="")
    for j in range(v):
        print(f"{j:4}", end="")
    print()
    for i in range(v):
        print(f"{i:2} |", end="")
        for j in range(v):
            val = matrix[i][j]
            if val == INF:
                print("   ∞", end="")
            else:
                print(f"{val:4}", end="")
        print()


def main():
    print("Алгоритм Флойда — Уоршелла")
    try:
        v = int(input("Введите количество вершин: "))
        if v <= 0:
            print("Ошибка: число вершин должно быть положительным.")
            return
    except ValueError:
        print("Ошибка ввода.")
        return

    graph = [[INF] * v for _ in range(v)]
    for i in range(v):
        graph[i][i] = 0

    print("Введите вес рёбер (для отсутствующего ребра введите 'inf'):")
    for i in range(v):
        for j in range(v):
            if i == j:
                continue
            while True:
                s = input(f"Вес {i} -> {j}: ").strip().lower()
                if s == "inf":
                    weight = INF
                    break
                try:
                    weight = float(s)
                    break
                except ValueError:
                    print("Некорректный ввод, попробуйте снова.")
            graph[i][j] = weight

    print("\nИсходная матрица:")
    print_matrix(graph)

    dist, neg_cycle = floyd_warshall(graph)

    if neg_cycle:
        print("\nОбнаружен отрицательный цикл! Кратчайшие пути не определены.")
    else:
        print("\nМатрица кратчайших расстояний:")
        print_matrix(dist)

if __name__ == "__main__":
    main()