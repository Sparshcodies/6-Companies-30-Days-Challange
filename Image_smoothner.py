img = [[100,200,100],[200,50,200],[100,200,100]]
n = len(img)
m = len(img[0])
for column in img:
    column.insert(0, None)
    column.append(None)
img.insert(0, [None]*(m+2))
img.append([None]*(m+2))
output_img = [[None]*m for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, m+1):
        neighbours = [img[i-1][j-1] , img[i-1][j] , img[i][j-1] , img[i][j] , img[i+1][j] , img[i][j+1] , img[i+1][j+1] , img[i-1][j+1] , img[i+1][j-1]]
        neigh = list(num for num in neighbours if num != None)
        # print(sum(neighbours),non)
        output_img[i-1][j-1] = sum(neigh) // len(neigh)
print(output_img)