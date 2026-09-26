class Solution:
    def subtractProductAndSum(self, n: int) -> int:
       mul = 1
       add = 0

       while n>0:
        place = n%10
        mul = mul*place
        add = add+place
        n //= 10

       return (mul-add)
