#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


Johnny = [5, 3, 3, 5, 4]
SB_Johnny = sum(Johnny) / len(Johnny)
Bilbo = [2, 2, 2, 3]
SB_Bilbo = sum(Bilbo) / len(Bilbo)
Steve = [4, 5, 5, 2]
SB_Steve = sum(Steve) / len(Steve)
Khendrik = [4, 4, 3]
SB_Khendrik = sum(Khendrik) / len(Khendrik)
Aaron = [5, 5, 5, 4, 5]
SB_Aaron = sum(Aaron) / len(Aaron)

SB_Svod = {'Johnny': SB_Johnny, 'Bilbo': SB_Bilbo, 'Steve': SB_Steve, 'Khendrik': SB_Khendrik, 'Aaron': SB_Aaron}

print(SB_Svod)

