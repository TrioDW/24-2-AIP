def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)

numbers = list(map(int, input().split()))
target = int(input())

indexes = two_sum(numbers, target)

print(f"indexes: ({indexes[0]}, {indexes[1]}), values: ({numbers[indexes[0]]}, {numbers[indexes[1]]})")
