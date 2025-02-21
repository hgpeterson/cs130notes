# Tarjan's Algorithm for Identifying Strongly Connected Components in a Dependency Graph

Motivation from project 4: 
- Up through project 3, a simple DFS traversal of the dependency graph is adequate to detect cycle-detection
- This no longer works in project 4 when `ISERROR()` is introduced
    - Must distinguish between nodes in cycles versus nodes that reference cycles but are not part of a cycle

Example: 

|   | A   | B   | C            |
|---|-----|-----|--------------|
| 1 | =B1 | =A1 | =ISERROR(B1) |

## Strongly Connected Components

Nodes in a cycle are called **strongly connected components (SCCs)**.
(A single node not in any cycle is a **trivial SCC**; a multiple-cell SCC is **non-trivial**).

## SCC Algorithms

Two widely used algos: Tarjan's and Kosaraju.
- Both built on top of DFS
- Tarjan's is a little easier to understand
- Tarjan's also generates a reverse topological sort over the nodes in the graph

## Tarjan's Algorithm (TA)

### Approach

TA operates on the entire graph.
- Iterate over all nodes in graph . . .
- If a node hasn't yet been visited, start a DFS traversal from that node
    - All SCCs reachable from that node are identified

```
def tarjan(graph):
    visited = set()
    for node in graph.nodes():
        if not nodeid. in visited:
            find_sccs(graph, node)

def find_sccs(graph, node):
    # TODO: Somthing with DFS?
```

### Node IDs and Lowlinks

- TA assigns increasing numeric IDs to nodes as it visits them
- Each SCC is identified by the node with the lowest ID in that SCC
    - This is called a node's **lowlink value**
- If each SCC in the graph is **condensed** down to a single node with an ID of the SCC's lowlink value:
    - The graph becomes a directed acyclic graph
    - A node $i$ is a predecessor of node $j$ if $i < j$

### Computing Lowlinks

As TA traverses the graph, lowlink values are propagated according to specific rules:
- When the node is visited for the first time, the next available ID is assigned to the node and the lowlink value is set to its own ID value
- Neighbor nodes fall into two categories:
    1. The neighbor has not been visited yet
        - Recursively invoke algo on neighbor, then update the lowlink value (`node.lowlink = min(node.lowlink, neighbor.lowlink)`)
    2. The neighbor has already been visited
        - Are we inside a cycle? Need more information. . .

To solve second category, TA must discern between different kinds of links:
- **Forward-links** are identified via DFS to previously-unvisited nodes
- Non-trivial SCCs will include at least one **back-link**, pointing to some node entered earlier in the DFS 
- We may also find **cross-links** between subtrees within the graph
    - *We don't care about these, but how do we distinguish between cross- and back-links?*

Need to maintain a **stack of nodes** that TA has entered during DFS (*separate* from whatever is used for DFS).
Stack rules:
- When we enter a node, it is always pushed onto the stack
- Nodes are only popped off when we identify SCCs

If we are in a non-trivial SCC, we will eventually reach a node in the SCC we have already entered, but have not left yet! 
- Example: If we are at node `5`, the stack is `[1, 2, 5]`, and we can reach `2` again, we have found a non-trivial SCC `[2, 5]`.
- When this happens, the lowlink is updated to be the same as the other node's ID (see references at end for alternative approach)
```
if neighbor.id in stack:
    my.lowlink = min(my.lowlink, neighbor.id)
```

### Updating the Stack

But **how do we update the stack?**
- When ready to leave node, compare its ID and lowlink values
- If they are the same, then this node is the starting point of a SCC
    - Pop all nodes in the SCC off the stack until we have also popped off the current node's ID
    - Record these nodes into a data structure representing the SCC

### Wikipedia Implementation

```
algorithm tarjan is
    input: graph G = (V, E)
    output: set of strongly connected components (sets of vertices)
   
    index := 0
    S := empty stack
    for each v in V do
        if v.index is undefined then
            strongconnect(v)
   
    function strongconnect(v)
        // Set the depth index for v to the smallest unused index
        v.index := index
        v.lowlink := index
        index := index + 1
        S.push(v)
        v.onStack := true
      
        // Consider successors of v
        for each (v, w) in E do
            if w.index is undefined then
                // Successor w has not yet been visited; recurse on it
                strongconnect(w)
                v.lowlink := min(v.lowlink, w.lowlink)
            else if w.onStack then
                // Successor w is in stack S and hence in the current SCC
                // If w is not on stack, then (v, w) is an edge pointing to an SCC already found and must be ignored
                // See below regarding the next line
                v.lowlink := min(v.lowlink, w.index)
      
        // If v is a root node, pop the stack and generate an SCC
        if v.lowlink = v.index then
            start a new strongly connected component
            repeat
                w := S.pop()
                w.onStack := false
                add w to current strongly connected component
            while w ≠ v
            output the current strongly connected component
```
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm

## References

- [CMU Lecture Notes](https://www.cs.cmu.edu/~15451-f18/lectures/lec19-DFS-strong-components.pdf)
- [A good visual explanation on YouTube](https://www.youtube.com/watch?v=wUgWX0nc4NY)
    - This implementation differs slightly from the one here, see the CMU notes for the alternate implementation

## A Common Variation of TA

- *Always* start a DFS on each neighbor visited
- Different lowlink update: `my.lowlink = min(my.lowlink, neighbor.lowlink)` instead of `neighbor.id`
    - Still works, just new interpretation of lowlink

## Implementation Notes

- Use helper classes to manage the state required for TA
    - Don't be like Wiki's implementation! 🤮
- Recursive version is straightforward. . . making it iterative is harder
    - The variation above may be a bit easier in this sense