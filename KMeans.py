import csv
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt

newcentroids = []
itercount = 0
objfuncval = []
finalobjfuncval = 0.0

#getting first points
def get_first(k, points):
    return points[0:k]

#objective function method
def objfunc(lcentroids, lclusters):
    num = 0

    for i in range(len(lcentroids)):
        centroid = lcentroids[i]
        cluster = lclusters[i]
        for point in cluster:
            num += (distance.euclidean(centroid, point))**2

    return num

#computing centroids getting means
def compute_centroids(lclusters):
    lcentroids = []

    for cluster in lclusters:
        lcentroids.append(np.mean(cluster, axis=0))

    return lcentroids

#kmeans main algrotihm in a recursive iteration
def kmeans(k, lcentroids, points, iter, getinitial):
    lclusters = [[] for i in range(k)]

    global newcentroids
    global itercount
    global objfuncval
    global finalobjfuncval

    for i in range(len(points)):
        point = points[i]
        belongs_to_cluster = closest_centroid(point, lcentroids)
        lclusters[belongs_to_cluster].append(point)

    new_centroids = compute_centroids(lclusters)

    notequal = False
    for a1 in range(len(lcentroids)):
        if distance.euclidean(lcentroids[a1], new_centroids[a1]) >= 0.0001:
            notequal = True
            break
    objval = objfunc(new_centroids, lclusters)
    if notequal and not getinitial:
        objfuncval.append(objval)
        lclusters = kmeans(k, new_centroids, points, iter+1, getinitial)
    else:
        itercount = iter
        newcentroids = lcentroids
        finalobjfuncval = objval
    return lclusters

def closest_centroid(point, lcentroids):
    min_distance = float('inf')
    belongs_to_cluster = None
    for j in range(len(lcentroids)):
        centroid = lcentroids[j]
        dist = distance.euclidean(point, centroid)
        if dist < min_distance:
            min_distance = dist
            belongs_to_cluster = j

    return belongs_to_cluster

#reading txt file
def readtxt(filename):
    ifile = open(filename, "r")
    reader = csv.reader(ifile, delimiter=",")

    rownum = 0
    a = []

    for row in reader:
        a.append(row[0:2])
        rownum += 1

    ifile.close()
    a1 = []
    for i in a:
        a1.append(list(map(float, i)))
    return a1

def mainfunc(ldata, k, getinitial):

    global newcentroids
    global itercount
    global objfuncval
    global finalobjfuncval

    newcentroids = []
    itercount = 0
    objfuncval = []
    finalobjfuncval = 0.0

    # k-means picking the first k points as centroids
    lcentroids = get_first(k, ldata)
    lclusters = kmeans(k, lcentroids, ldata, 1, getinitial)
    lcluster_assigned =  []

    for i in ldata:
        bb = 0
        clusterassigned = False
        for j in lclusters:
            for kk in j:
                if i == kk:
                    clusterassigned = True
                    lcluster_assigned.append(bb)
                    break
                if clusterassigned:
                    break
            if clusterassigned:
                break
            bb = bb + 1
    # Create the graph based on the amount of clusters required
    cluster_assigned = np.array((lcluster_assigned))
    data = np.array((ldata))
    centroids = np.array(newcentroids)

    group_colors = ['red', 'lightgreen', 'cyan', 'brown', 'yellow', 'purple', 'gray', 'maroon']
    colors = [group_colors[j] for j in cluster_assigned]
    plt.scatter(data[:, 0], data[:, 1], color=colors, alpha=0.5)

    # Create the centroids for the graph and use a specific colour depending on amount
    colorCentres = ['maroon', 'green', 'blue', 'black', 'maroon', 'black', 'black', 'black']
    colorCentre = [colorCentres[cC] for cC in range(0, k)]
    plt.scatter(centroids[:, 0], centroids[:, 1], color=colorCentre)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()

    if not getinitial:
        plt.plot(range(1, itercount), objfuncval)
        plt.xlabel('K')
        plt.ylabel('Objective Function Value')
        plt.show()
        print ('Total iteration count' + str(itercount))
        print ('Final objective function value' + str(finalobjfuncval))

if __name__ == "__main__":
    ldata1 = readtxt('data1.txt')
    ldata2 = readtxt('data2.txt')
    ldata3 = readtxt('data3.txt')

    #data1 k=3, initial
    mainfunc(ldata1, 3, True)
    #data1 k=3, final
    mainfunc(ldata1, 3, False)
    #data1 k=7, initial
    mainfunc(ldata1, 7, True)
    #data1 k=7, final
    mainfunc(ldata1, 7, False)
    #data2 k=5, initial
    mainfunc(ldata2, 5, True)
    #data2 k=5, final
    mainfunc(ldata2, 5, False)
    #data3 k=8, initial
    mainfunc(ldata3, 8, True)
    #data3 k=8, final
    mainfunc(ldata3, 8, False)

