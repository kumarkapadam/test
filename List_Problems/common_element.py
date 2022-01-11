# finding  common elements in two lists

group1 = ['kumar', 'veera', 'raju', 'kiran','sasi']
group2 = ['santhosh', 'sasi', 'sankar', 'syam', 'kumar']

g1 = set(group1)
g2 = set(group2)

g3 = g1.intersection(g2)
common = list(g3)
print("common name is ", common)
