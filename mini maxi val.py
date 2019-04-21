list = [5,7,9,10,11,12,45,73,125,13]

maxVal = 0
minVal = 0

for i in range (0,  len(list),1):
      maxVal = max(maxVal,list[i])
      minVal = min(minVal,list[i])

print("max:",maxVal)
print("min:",minVal)
   
