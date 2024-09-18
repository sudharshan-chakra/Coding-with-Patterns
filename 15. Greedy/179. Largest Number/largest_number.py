class Solution:
    def compare(self,num1, num2):
        if num1+num2 > num2+num1:
            return 1
        else:
            return -1
        
    def largestNumber(self, nums: List[int]) -> str:
        numstring = [str(i) for i in nums]

        numstring = sorted(numstring,key=cmp_to_key(self.compare))

        return str(int(''.join(numstring)))