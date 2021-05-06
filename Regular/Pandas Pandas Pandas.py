import numpy as np
n = int(input())
cluster1 = []
cluster2 = []
centroid1 = np.array([0,0])
centroid2 = np.array([2,2])
data_p = []
for i in range(n):
    a = input()
    try :
        a = np.array(a.split(' ')).astype('float')
    except :
        continue
    data_p.append(list(a))
data_p = np.array(data_p)


# for i in data_p:
#     if abs((i**2 - centroid1**2).sum()**1/2) < abs((i**2 - centroid2**2).sum()**1/2):
#         cluster1.append(i)
#     elif abs((i**2 - centroid1**2).sum()**1/2) == abs((i**2 - centroid2**2).sum()**1/2):
#         cluster1.append(i)
#     else:
#         cluster2.append(i)

# cluster1, cluster2 = np.array(cluster1), np.array(cluster2)
# print('data points :', data_p)
# print('Cluster 1 :', cluster1)
# print('Cluster 2 :', cluster2)
# print()
# # abs((a**2 - b**2).sum()**1/2) Euclidean

# centroid2 = cluster2.mean()
# centroid1 = cluster1.mean()

# cluster1 = []
# cluster2 = []
# for i in data_p:
#     if abs((i**2 - centroid1**2).sum()**1/2) < abs((i**2 - centroid2**2).sum()**1/2):
#         cluster1.append(i)
#     elif abs((i**2 - centroid1**2).sum()**1/2) == abs((i**2 - centroid2**2).sum()**1/2):
#         cluster1.append(i)
#     else:
#         cluster2.append(i)

# print('Cluster 1 :', np.array(cluster1))
# print('Cluster 2 :', np.array(cluster2))

while True:
    # Get Euclidean Distance and add it to its cluster
    for i in data_p:
        if abs((i**2 - centroid1**2).sum()**1/2) < abs((i**2 - centroid2**2).sum()**1/2):
            cluster1.append(i)
        elif abs((i**2 - centroid1**2).sum()**1/2) == abs((i**2 - centroid2**2).sum()**1/2):
            cluster1.append(i)
        else:
            cluster2.append(i)
    cluster1 = np.array(cluster1)
    cluster2 = np.array(cluster2)
    new_centroid1 = np.array([cluster1[:,0].mean().round(2), cluster1[:,1].mean().round(2)])
    new_centroid2 = np.array([cluster2[:,0].mean().round(2), cluster2[:,1].mean().round(2)])


    # print(f'''Old Centroid : {centroid1} and {centroid2}
    # New Centroid : {new_centroid1} and {new_centroid2}''')
    if list(new_centroid1) != list(centroid1) or list(new_centroid2) != list(centroid2):
        centroid1 = new_centroid1
        centroid2 = new_centroid2
        cluster1 = []
        cluster2 = []
    else :
        print(new_centroid1)
        print(new_centroid2)
        break

