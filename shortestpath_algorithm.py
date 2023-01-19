# Backend >> Calculation part
# Not complete
# Create a left-to-right graph 
# distance * 60% + lane * 40% = result for choose
# topnode for distance = n * 2

node = []
distance = []
lane = []
caldist = []
shortnode = []
longnode = []
check = 0
print("Shortest path app")
print("default node >= 3")
o = int(input("amount of node >> "))

if o%2 == 0:
    check = 2
elif o%2 == 1:
    check = 3

start = ord('A')
for i in range(o):
    node.append(chr(start + i))

# for i in range(o):
#     n = input("(%d) Name node >> " % (i+1))
#     node.append(n)

if o == 3:
    # node == 3
    for i in range(len(node) - 1):
        d = input("distance %s to %s >> " % (node[i], node[i+1]))
        distance.append(d)
        l = input("lane %s to %s >> " % (node[i], node[i+1]))
        lane.append(l)

    np = ", ".join(node)
    dp = ", ".join(distance)
    l = ", ".join(lane)
    print("\nnode = %s" % (np))
    print("\ndistance = %s" % (dp))
    print("\nlane = %s\n" % (l))

    for j in range(len(distance)):
        dist = (float(distance[j]) * (60/100)) + (float(lane[j]) * (40/100))
        caldist.append(dist)

    cd = " , ".join(str(i) for i in caldist)
    print("\ncaldist = %s" % (cd))
    shortnode.append(node[0])
    longnode.append(node[0])

    if caldist[0] > caldist[1]:
        shortnode.append(node[2])
        longnode.append(node[1])
    elif caldist[0] < caldist[1]:
        shortnode.append(node[1])
        longnode.append(node[2])
    
    print("shortnode = %s" % (" -> ".join(shortnode)))
    print("longnode = %s" % (" -> ".join(longnode)))

elif o > 3:
    #node > 3
    p1 = 1
    for i in range(o - check):
        d1 = input("distance %s to %s >> " % (node[i], node[p1]))
        l1 = input("lane %s to %s >> " % (node[i], node[p1]))
        distance.append(d1)
        lane.append(l1)
        # node is odd
        if o-1 == p1:
            break
        d2 = input("distance %s to %s >> " % (node[i], node[p1+1]))
        l2 = input("lane %s to %s >> " % (node[i], node[p1+1]))
        distance.append(d2)
        lane.append(l2)
        p1 += 2
    
    np = ", ".join(node)
    dp = ", ".join(distance)
    l = ", ".join(lane)
    print("\nnode = %s" % (np))
    print("\ndistance = %s" % (dp))
    print("\nlane = %s\n" % (l))

    for j in range(len(distance)):
        dist = (float(distance[j]) * (60/100)) + (float(lane[j]) * (40/100))
        caldist.append(dist)

    cd = " , ".join(str(i) for i in caldist)
    print("\ncaldist = %s\n" % (cd))
    shortnode.append(node[0])
    longnode.append(node[0])

    p2 = 1
    p3 = 0
    for k in range(o - check):
        l = []
        print("%s to %s = %f" % (node[k], node[p2], caldist[p3]))
        l.append(node[p2])
        print(l)
        # node is odd
        if o-1 == p2:
            break
        print("%s to %s = %f" % (node[k], node[p2+1], caldist[p3+1]))
        l.append(node[p2+1])
        print(l)
        l.clear()
        p2 += 2
        p3 += 2
    
    # p2 = 1
    # for i in node:
    #     if caldist[p2] > caldist[p2+1]:
    #         shortnode

    # print("shortnode = %s" % (" -> ".join(shortnode)))
    # print("longnode = %s" % (" -> ".join(longnode)))


# np = ", ".join(node)
# dp = ", ".join(distance)
# l = ", ".join(lane)
# print("\nnode = %s" % (np))
# print("\ndistance = %s" % (dp))
# print("\nlane = %s" % (l))


