# Reduced Ordered Binary Decision Diagram
A Boolean function can be represented as a rooted, directed, acyclic graph, which consists of several (decision) nodes and two terminal nodes. The two terminal nodes are labeled 0 (FALSE) and 1 (TRUE). Each node u is labeled by a Boolean variable x and has two child nodes called low child and high child. The edge from node u to a low (or high) child represents an assignment of the value FALSE (or TRUE, respectively) to variable x. Such a BDD is called 'ordered' if different variables appear in the same order on all paths from the root. A BDD is said to be 'reduced' if the following two rules have been applied to its graph:

1. Merge any isomorphic subgraphs.

2. Eliminate any node whose two children are isomorphic.

<p align="center">
<img src="https://user-images.githubusercontent.com/58945374/117542249-79506800-b035-11eb-9a86-b956359f7c64.png">
</p>
