"""
This is submission docstring
"""


class Subset():
    def __init__(self, s, t):
        if len(s) > len(set(s)):
            raise ValueError(f"{s} contains duplicates")
        self.S = s
        self._target = t
        self.Col = [set()]
        self._max_subset = set()
        self._max_sum = 0

    @property
    def max_subset(self):
        return self._max_subset

    @property
    def sum(self):
        return self._max_sum

    def __str__(self):
        return ('\n'.join([str(set_item) for set_item in self.Col])
                + '\n' + '_' * 20 + '\n' + str(self.sum))

    def __eq__(self, other):
        return [all((getattr(self, "S") == getattr(other, "S")) for number in self.S)]

    def add(self, item):
        itemset = set()
        itemset.add(item)
        update = [i.copy() for i in self.Col if len(i) != 0]
        for i in update:
            i = i.add(item)
        if itemset not in update:
            update.append(itemset)
        for i in update:
            if i:
                current_sum = 0
                current_set = set()
                for k in i:
                    current_sum += self.S[k]
                    if current_sum > self._target:
                        current_sum = 0
                        break
                if 0 <= current_sum <= self._target:
                    current_set = i
                    if self.sum < current_sum:
                        self._max_sum = current_sum
                        self._max_subset = [self.S[i] for i in current_set]
        return update

    def find_power_set(self):
        for i in range(0, len(self.S)):
            update = self.add(i)
            for item in update:
                if item not in self.Col:
                    self.Col.append(item)


def main():
    print("Test1" + "_" * 20)
    t = 200
    s = []
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("_" * 20)
    print("Test2-1" + "_" * 20)
    t = 200
    s = [19]
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("Test2-2" + "_" * 20)
    t = 19
    s = [19]
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("_" * 20)
    print("Test2-3" + "_" * 20)
    t = 10
    s = [19]
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("_" * 20)
    print("Test3-1" + "_" * 20)
    t = 2
    s = [14, 17]
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("Test3-2" + "_" * 20)
    t = 15
    s = [14, 17]
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("_" * 20)
    print("Test3-3" + "_" * 20)
    t = 50
    s = [14, 17]
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("_" * 20)
    print("Test4" + "_" * 20)
    t = 200
    s = [20, 12, 22, 15, 25, 19, 29, 18, 11, 13, 17]
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("_" * 20)
    print("Test5" + "_" * 20)
    t = 50
    s = [25, 27, 3, 12, 6, 15, 9, 30, 21, 19]
    subsets = Subset(s, t)
    subsets.find_power_set()
    print(f"{subsets.max_subset=}")
    print(f"{subsets.sum=}")
    print("_" * 20)


if __name__ == "__main__":
    main()
