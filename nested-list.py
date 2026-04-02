if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = sorted(list(set([x[1] for x in students])))
    second_lowest_score = scores[1]
    result_names = [x[0] for x in students if x[1] == second_lowest_score]
    result_names.sort()
    for name in result_names:
        print(name)
