class Solution:
    def distMoney(self, money: int, children: int) -> int:

        money -= children

        count = 0

        if money < 0:
            return -1

        while money - 7 >= 0:

            money -= 7
            count +=1
            
            if count == children and money >0:
                return count -1

        if money == 3 and count != 0 and count  == children-1:
            return count-1

        return count
