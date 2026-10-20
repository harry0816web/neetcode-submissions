class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sz = len(position)
    
        cars = sorted(zip(position, speed), reverse=True)
        # cars = [(pos, spd), ...]，tuple 預設依第一個元素 pos 排序

        # use stack to track current fleets id
        stack = []
        stack.append(0)   

        step = []
        for i in range(0, sz):
            step.append((target - cars[i][0]) / cars[i][1]) 
        # print(cars) 
        # print(step)
        
        for i in range(1, sz):
            # print("last", step[stack[-1]])
            # won't catch up
            if step[i] > step[stack[-1]]:
                stack.append(i)
            else:
                # join fleet (same position, same speed => same step)
                continue


                
    

        return len(stack)

# 0 1 4 7
# 1 2 2 1
# step
# 10 5 3 3

        
            

        
