from collections import defaultdict
from typing import List, Dict


# O(n^2)
def twoSumInefficent(nums: List[int], target: int) -> List[int]:
    res = []
    for i, n in enumerate(nums):
        for j, v in enumerate(nums):
            if i is not j:
                if n + v == target:
                    res.extend([i, j])
                    return res
    return res


# T-O(n) S-O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    res: List[int] = []
    different: Dict[int, int] = defaultdict(int)

    for index, value in enumerate(nums):
        if value in different and different[value] != index:
            res.extend([different[value], index])
            break
        different[target - value] = index

    return res


class Tests:
    def test1(self):
        assert twoSum([2, 7, 11, 15], 9) == [0, 1]

    def test2(self):
        assert twoSum([3, 2, 4], 6) == [1, 2]

    def test3(self):
        assert twoSum([3, 3], 6) == [0, 1]

    def test4(self):
        assert twoSum([], 6) == []

    def test5(self):
        assert twoSum([-1, -2, -6, 3, 4, 6], 5) == [0, 5]
