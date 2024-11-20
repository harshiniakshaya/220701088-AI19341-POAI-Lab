def water_jug(j1c,j2c,target):
    visited = set()
    stack = [(0,0)]
    while(stack):
        j1,j2=stack.pop()
      
        if(j1==target or j2==target or j1+j2==target):
            print("j1 ",j1,"; j2",j2)
            if(j1==target):
                j2=0
                print("j1 ",j1,"; j2",j2)
            elif(j2==target):
                j1=0
                print("j1 ",j1,"; j2",j2)
                j1=j2
                j2=0
                print("j1 ",j1,"; j2",j2)
            else:
                j1+=j2
                j2=0
                print("j1 ",j1,"; j2",j2)
                
            print(f"Solution found: Jug1 = {j1}, Jug2 = {j2}")
            return True
        
        visited.add((j1,j2))
        print("j1 ",j1,"; j2",j2)
        
        if (j1c,j2) not in visited:
            stack.append((j1c,j2))

            
        if (j1,j2c) not in visited:
            stack.append((j1,j2c))

            
        if (0,j2) not in visited:
            stack.append((0,j2))

        
        if (j1,0) not in visited:
            stack.append((j1,0))

            
        pour_12 = min(j1,j2c-j2)
        if (j1-pour_12,j2+pour_12) not in visited:
            stack.append((j1-pour_12,j2+pour_12))
        
        pour_21 = min(j1c-j1,j2)
        if (j1+pour_21,j2-pour_21) not in visited:
            stack.append((j1+pour_21,j2-pour_21))
    return False;
j1c=4
j2c=3
target=2
water_jug(j1c,j2c,target)
'''
j1  0 ; j2 0
j1  0 ; j2 3
j1  3 ; j2 0
j1  3 ; j2 3
j1  4 ; j2 2
j1  0 ; j2 2
j1  2 ; j2 0
Solution found: Jug1 = 2, Jug2 = 0
'''
