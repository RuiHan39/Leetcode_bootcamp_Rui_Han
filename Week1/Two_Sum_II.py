class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        while i < len(numbers):
            rest = target - numbers[i]
            restnum = numbers[i+1::]
            if rest in restnum:
                index2 = restnum.index(rest)+i+2
                return [i+1,index2]
            else:
                i=i+1
