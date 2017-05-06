It's time to show off what you've learned about technical interviewing!

For this project, you will be given five technical interviewing questions on a variety of topics discussed in the technical interviewing course. You should write up a clean and efficient answer in Python, as well as a text explanation of the efficiency of your code and your design choices. A qualified reviewer will look over your answer and give you feedback on anything that might be awesome or lacking—is your solution the most efficient one possible? Are you doing a good job of explaining your thoughts? Is your code elegant and easy to read?

Answer the following questions:

### Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

from itertools import permutations

def question1(s, t):
    if t == "":
        return True
    elif t == None or s == None:
        return False
    elif len(s) < len(t):
        return False
    else:
        for l in t:
            if s.find(l) == -1:
                break
            else:
                for p in permutations(t):
                    if s.find(''.join(p)) != -1:
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
Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

def question2(a):
    longest = ""
    if a == "":
        return a
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


### Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)


### Question 4
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.

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
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

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