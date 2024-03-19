names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

#  Решение


def gen_dict(names, salary, bonus) -> dict:
    return {
        name: sal * int(bon[:-1]) / 100 for name, sal, bon in zip(names, salary, bonus)
    }


print(gen_dict(names, salary, bonus))

#  Эталонное решение

result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)
