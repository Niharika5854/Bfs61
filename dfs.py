def main():  
 
        #     0  1  2  3  4  5  6
        #  0  0  1  1  0  0  0  0
        #  1  1  0  0  1  0  0  0
        #  2  1  0  0  0  1  1  0
        #  3  0  1  0  0  0  0  0
        #  4  0  0  1  0  0  0  1
        #  5  0  0  1  0  0  0  0
        #  6  0  0  0  0  1  0  0
 
        # The graph's adjacency matrix
    matrix =[[0,  1,  1,  0,  0,  0,  0],
                  [1,  0,  0,  1,  0,  0,  0],
                  [1,  0,  0,  0,  1,  1,  0],
                  [0,  1,  0,  0,  0,  0,  0],
                  [0,  0,  1,  0,  0,  0,  1],
                  [0,  0,  1,  0,  0,  0,  0],
                  [0,  0,  0,  0,  1,  0,  0]]
                
  # The visited array
    visited = [0,0,0,0,0,0,0]
 
    # Add the start node to the stack
    # Node '0' in this case
    stack = [0]
 
    # Set the visited value of node 0 to visited
    visited[0] = 1
 
    # Pop the stack
    node = stack.pop(len(stack) - 1);
    print(node)
 
    while True:
 
                # Iterate over the total amount of nodes
        for x in range (0, len(visited)):
 
                        # Check if route exists and that node isn't visited
            if matrix[node][x] == 1 and visited[x] == 0:
 
                                # Visit node
                visited[x] = 1;
 
                                # Push the element in the stack
                stack.append(x)
 
        # When queue is empty, break        
        if len(stack) == 0:
 
            break;
 
        else:
 
                        # Pop the element from the stack
            node = stack.pop(len(stack) - 1)
            print(node)
     
if _name_ == "_main_":
    main()