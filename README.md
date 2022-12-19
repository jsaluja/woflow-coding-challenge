# woflow-coding-challenge-questions

1. **What is the total number of unique node IDs?**

    30

2. **What is the most common node ID?**

    a06c90bf-e635-4812-992e-f7b1e2408a3f
    
# Usage
    python woflow.py
    
# Approach
    Standard BFS with Queue, visited set. 
    Track frequency counter in a dictionary to return the most common node
    
    DFS would work as well
    
# Complexity
    
    Space - O(N) - BFS queue, DFS stack
    Time - O(N) - Visit all nodes at least once
