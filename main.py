import numpy as np
import math
import matplotlib.pyplot as plt


def task_2_1_2():
    x = 0.1334

    xi_list = [
        0.115,
        0.120,
        0.125,
        0.130,
        0.135,
        0.140
    ]
    xi_list = np.array(xi_list)

    yi_list = [
        8.65729,
        8.29329,
        7.95829,
        7.64893,
        7.36235,
        7.09613,
    ]
    yi_list = np.array(yi_list)

    t = (x - xi_list[0]) / 0.005
    t_min_i = t - np.array([i for i in range(6)])
    print(t_min_i)
    print(np.prod(t_min_i))
    ci = np.array([(-1) ** (5 - i) * math.factorial(i) * math.factorial(5 - i) for i in range(6)])
    print(ci)
    ci_mul_tmini = t_min_i * ci
    print(ci_mul_tmini)
    print(yi_list / ci_mul_tmini)
    print(np.sum(yi_list / ci_mul_tmini))
    print(np.prod(t_min_i) * np.sum(yi_list / ci_mul_tmini))


def task_2_2():
    data = """
0,45 20,1946
0,46 19,6133
0,47 18,9425
0,48 18,1746
0,49 17,3010
0,50 16.3123
0,51 15,1984
0,52 13,9484
0,53 12,5508
0,54 10,9937
0,55 9,2647
0,56 7,3510""".replace(",", ".").strip()

    data = [*map(lambda x: x.split(" "), data.split("\n"))]
    n = len(data)
    xi = [*map(lambda x: float(x[0]), data)]
    yi = [*map(lambda x: float(x[1]), data)]
    print(*xi)
    print(*yi)

    delta_1 = np.array([yi[i + 1] - yi[i] for i in range(n) if i + 1 < n])
    print(delta_1)
    delta_2 = np.array([delta_1[i + 1] - delta_1[i] for i in range(len(delta_1)) if i + 1 < len(delta_1)])
    print(delta_2)
    delta_3 = np.array([delta_2[i + 1] - delta_2[i] for i in range(len(delta_2)) if i + 1 < len(delta_2)])
    print(delta_3)


def task_2_3():
    xi = np.array([*map(float, "10 20 40 60 90 110 120 130 140 150".split(' '))])
    yi = np.array([*map(float, "1,5 1,8 3 3,9 4,8 5,5 5,7 7 8,1 9,4".replace(",", ".").split(' '))])

    print(xi, end=" ")
    print(np.sum(xi))

    print(yi, end=" ")
    print(np.sum(yi))

    print(xi**2, end=" ")
    print(np.sum(xi**2))

    print(xi*yi, end=" ")
    print(np.sum(xi*yi))

    k, b = np.linalg.solve([[np.sum(xi**2), np.sum(xi)], [np.sum(xi), len(xi)]], [np.sum(xi*yi), np.sum(yi)])

    print(k, b)

    print("F=", k * 160 + b)

    x = np.linspace(0, 160, 160) * k + b

    plt.plot(xi, yi, x)
    plt.show()


def task_2_4():
    xi = np.array([*map(float, "1 1,2 1,4 1,7 2 2,4 2,8 3,2 3,6 4".replace(",", ".").split(' '))])
    yi = np.array([*map(float, "1100 920 850 830 800 785 770 760 750 745".replace(",", ".").split(' '))])

    print(xi, end=" ")
    print(np.sum(xi))

    print(yi, end=" ")
    print(np.sum(yi))

    print(xi**2, end=" ")
    print(np.sum(xi**2))

    print(xi**3, end=" ")
    print(np.sum(xi**3))

    print(xi**4, end=" ")
    print(np.sum(xi**4))

    print(xi**2*yi, end=" ")
    print(np.sum(xi**2*yi))

    print(xi*yi, end=" ")
    print(np.sum(xi*yi))

    print(xi*yi, end=" ")
    print(np.sum(xi*yi))

    k, b = np.linalg.solve([[np.sum(xi**2), np.sum(xi)], [np.sum(xi), len(xi)]], [np.sum(xi*yi), np.sum(yi)])

    print(k, b)

    print("F=", k * 160 + b)

    x = np.linspace(0, 160, 160) * k + b

    plt.plot(xi, yi, x)
    plt.show()


if __name__ == '__main__':
    task_2_4()
