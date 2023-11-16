products = ['carpet', 'cart', 'car', 'camera', 'crate']
search = 'camera'
result = []
length = len(search)
products.sort()
n = len(products)
for i in range(1,length):
    tmp = []
    for j in range(n):
        if products[j][:i] == search[:i]:
            tmp.append(products[j])
    tmp = sorted(tmp)
    result.append(tmp[:3])
result = sorted(result)
print(result)