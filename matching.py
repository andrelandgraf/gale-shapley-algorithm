
list_a = ["a1", "a2", "a3", "a4"]
list_b = ["b1", "b2", "b3", "b4"]

if len(list_a) != len(list_b):
    print("Error! Lists a and b have to have the same length")

length = len(list_a)

# index in tuple says how valuable the element is. length-1 is most valuable element for the watched object.
# a1 wants to pair up with b4 the most, and does like b1 the less.
# b1 likes a1 the least and prefers to be matched with a4
a_preferences = [("b1", "b2", "b3", "b4"), ("b2", "b1", "b3", "b4"), ("b1", "b2", "b3", "b4"), ("b4", "b3", "b2", "b1")]
b_preferences = [("a1", "a2", "a3", "a4"), ("a3", "a1", "a2", "a4"), ("a1", "a4", "a3", "a2"), ("a4", "a3", "a1", "a2")]

# let all a of list_a point to the least valuable thing possible
# let all b of list_b point to the most valuable thing possible
a_graph = list()
b_graph = list()
for i, a in enumerate(list_a):
    # match all a with top and all b with bottom
    a_graph.append((a, -1))
    b_graph.append((list_b[i], length))


# start matching: stop if all b do have another partner then bottom
# partner means: there is a edge from b -> a and an edge from this a back to b
finished = False
while not finished:
    # we hope to get finished in the next iteration
    finished = True
    for i, b in enumerate(list_b):
        # get the preferences of this b
        preferences = b_preferences[i]
        # edge is tuple (b, index) with index being an index to an a of list_a or -1 / length as null pointer
        edge = b_graph[i]
        index = edge[1]

        single = False
        if index < length:
            # get current matched a
            a = preferences[index]
            # get index of this a in list_a
            i_of_a = list_a.index(a)
            # get matching index of current watched b for this a
            a_b_index = a_preferences[i_of_a].index(b)
            # get index of current matched b
            a_match = a_graph[i_of_a][1]
            if a_match != a_b_index:
                # a has new b -> current b has to match again
                single = True

        if index == length or single:
            # match this b with an a as this b was not matched yet
            # we can assure that index will never reach -1 as length of list_b = length of list_b
            # if we still have this b with matching index = length,
            # then there must also be an unmatched a with matching index = -1
            while index >= 0:
                index = index - 1
                # get next best possible candidate for this b
                a = preferences[index]
                # get index of this a in list_a
                i_of_a = list_a.index(a)
                # get current match of the candidate
                a_match = a_graph[i_of_a][1]
                # get index of current watched b for this a
                a_b_index = a_preferences[i_of_a].index(b)
                # check if the match is higher ranked for a then the current b
                if a_b_index > a_match:
                    # a likes current b more then his match
                    # match b and a
                    a_graph[i_of_a] = (a, a_b_index)
                    b_graph[i] = (b, index)
                    if a_match != -1:
                        # we just made one b single again, so we have to do one more iteration to fix that
                        finished = False
                    break

# result
result = list()
for i, a in enumerate(list_a):
    index_b = a_graph[i][1]
    b = a_preferences[i][index_b]
    result.append((a, b))

# result
validate_result = list()
for i, b in enumerate(list_b):
    index_a = b_graph[i][1]
    a = b_preferences[i][index_a]
    validate_result.append((b, a))

print("\n")
print(result)
print("\n")
print(validate_result)