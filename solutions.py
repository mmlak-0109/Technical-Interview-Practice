### Question 1

def question1(s, t):
    """The inputs are two strings s and t.  The algorithm determines whether some anagram of t is a substring of s and returns a boolean of True or False.  The for loop runs through the length of string s, checking whether the sorted string t is equal to a sorted substring in string s with a length of string t.
    """

    if s == None or t == None:
        return False

    else:
        for i in range(len(s)):
            if sorted(s[i:(i+len(t))]) == sorted(t):
                return True

        return False

#returns True
print question1("udacity", "ad")
#returns True
print question1("udacious", "")
#returns False
print question1("notudacious", "sorry")
#returns False
print question1("atrocious", "supercalifragilisticexpialidocious")
#returns False
print question1("igotnothing", None)





### Question 2

def question2(a):

    longest = ""

    if a == None:
        return "not a string"

    else:
        while a != a[::-1]:
            s = a
            a1 = a[1:]
            a2 = a[:-1]

            while a1 != a1[::-1]:
                a1 = a1[1:]
            else:
                s = a1
                if len(s) > len(longest):
                    longest = s

            while a2 != a2[::-1]:
                a2 = a2[:-1]
            else:
                s = a2
                if len(s) > len(longest):
                    longest = s

            a = a[1:-1]

        if len(a) > len(longest):
            longest = a

    return longest

#returns "abccba"
print question2('abccbadef')
#returns "dbabd"
print question2('bbcdbabdef')
#returns "geeksskeeg"
print question2('forgeeksskeegfor')
#returns ""
print question2("")
#returns "not a string"
print question2(None)





### Question 3

parent = {}
rank = {}
def make_disjoint_set(vert):
    parent[vert] = vert #stores vertices as key and value for easy hashing
    rank[vert] = 0 #stores tree depth at zero to improve find() performance

def sort_edges_by_weight(G):
    edges = []

    for vert in G:
        for i in range(len(G[vert])):
            edge = sorted((vert, G[vert][i][0], G[vert][i][1]))
            edge = tuple(edge)
            if edge not in edges:
                edges.append(edge)

    edges = sorted(edges)

    return edges

def find(vert):
    if parent[vert] == vert:
        return parent[vert]

    else:
        return find(parent[vert])

def finish_mst(mst, edge):
    weight, vert1, vert2 = edge

    for vert in mst:
        if vert1 == vert:
            mst[vert].append((vert2, weight))
        elif vert2 == vert:
            mst[vert].append((vert1, weight))

def union(vert1, vert2):
    if rank[vert1] > rank[vert2]:
        parent[vert2] = vert1

    elif rank[vert2] > rank[vert1]:
        parent[vert1] = vert2

    else:
        parent[vert1] = vert2
        rank[vert2] += 1

def question3(G):
    mst = {}
    mst_edge_len = 0 #will keep track of the number of edges

    for vert in G:
        mst[vert] = []
        make_disjoint_set(vert)

    edges = sort_edges_by_weight(G) #sorts in ascending order

    for edge in edges:
        weight, vert1, vert2 = edge
        if find(vert1) != find(vert2):
            mst_edge_len += 1
            if mst_edge_len <= (len(G) - 1): #will stop adding edges if False to keep a cycle from forming
                finish_mst(mst, edge)
                union(vert1, vert2)

    return mst

G0 = {}

G1 = {'A':[]}

G2 = {'A': [('B', 2)],
      'B': [('A', 2)]}

G3 = {'A': [('B', 2)],
      'B': [('A', 2), ('C', 5)],
      'C': [('B', 5)]}

G4 = {'A': [('B', 2), ('C', 6), ('D', 7)],
      'B': [('A', 2), ('C', 5)],
      'C': [('B', 5), ('D', 1)],
      'D': [('A', 7), ('C', 1)]}

#returns {}
print question3(G0)
#returns {'A':[]}
print question3(G1)
#returns {'A': [('B', 2)], 'B': [('A', 2)]}
print question3(G2)
#returns {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
print question3(G3)
#returns {'A': [('B', 2)], 'C': [('D', 1), ('B', 5)], 'B': [('A', 2), ('C', 5)], 'D': [('C', 1)]}
print question3(G4)





### Question 4

def question4(T, r, n1, n2):
    if r == None:
        return None

    elif (n1 <= r <= n2) or (n1 >= r >= n2):
        return r

    elif n1 < r > n2:
        for index, child in enumerate(T[r]):
            if child == 1 and index < r:
                r = index
                return question4(T, r, n1, n2)

    else:
        for index, child in enumerate(T[r]):
            if child == 1 and index > r:
                r = index
                return question4(T, r, n1, n2)

#returns 3
print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

#returns 4
print question4([[0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 0]],
          2,
          3,
          5)

#returns 1
print question4([[0, 1, 0],
           [0, 0, 1],
           [0, 0, 0]],
          0,
          2,
          1)

#returns None
print question4([[0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]],
    3,
    2,
    2)





### Question 5

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def question5(ll, m):
    real_ll = ll
    point_m = ll

    for n in range(0, m):
        if real_ll == None:
            return None
        real_ll = real_ll.next

    while real_ll != None:
        real_ll = real_ll.next
        point_m = point_m.next

    return point_m.data

#Test 1
a = Node(2)
b = Node(4)
c = Node(6)
d = Node(8)
e = Node(10)

a.next = b
b.next = c
c.next = d
d.next = e

#returns 6
print question5(a,3)

#Test 2
a = Node(1)
b = Node(3)
c = Node(5)
d = Node(7)
e = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e

#returns 7
print question5(a,2)

#returns None
print question5(None, 5)