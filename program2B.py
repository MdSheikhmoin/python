def bin2Dec(val):
 rev=val[::-1]
 dec = 0
 i = 0
 for dig in rev:
 dec += int(dig) * 2**i
 i += 1
 
 return dec
def oct2Hex(val):
 rev=val[::-1]
 dec = 0
 i = 0
 for dig in rev:
 dec += int(dig) * 8**i
 i += 1
 list=[]
 while dec != 0:
 list.append(dec%16)
 dec = dec // 16
nl=[]
 for elem in list[::-1]:
 if elem <= 9:
 nl.append(str(elem))
 else:
 nl.append(chr(ord('A') + (elem -10)))
 hex = "".join(nl)
 
 return hex
num1 = input("Enter a binary number : ") 
print(bin2Dec(num1))
num2 = input("Enter a octal number : ")
print(oct2Hex(num2))
