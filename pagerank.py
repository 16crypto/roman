import numpy as np

# PageRank function
def page_rank(graph, d=0.85, iterations=10):

    n = len(graph)              # number of pages
    rank = np.ones(n) / n       # initial rank for all pages

    # Iterate multiple times to update ranks
    for _ in range(iterations):
        new_rank = np.ones(n) * (1-d) / n

        for page in range(n):
            for link in graph[page]:
                new_rank[link] += d * rank[page] / len(graph[page])

        rank = new_rank

    return rank


# Web graph (link structure)
graph = [
[1,2],    # Page 0 links to Page 1 and Page 2
[2],      # Page 1 links to Page 2
[0]       # Page 2 links to Page 0
]

# Calculate PageRank
result = page_rank(graph)

# Display results
for i, r in enumerate(result):
    print("Page", i, "Rank:", r)