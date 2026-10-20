class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sz = len(position)
    
        cars = sorted(zip(position, speed), reverse=True)
        # cars = [(pos, spd), ...]，tuple 預設依第一個元素 pos 排序

        # use stack to track current fleets id
        ahead_fleet_time = (target - cars[0][0]) / cars[0][1]
        cnt = 1
        for i in range(1, sz):
            step = (target - cars[i][0]) / cars[i][1]
            if step > ahead_fleet_time:
                ahead_fleet_time = step
                cnt += 1
            else:
                # join fleet (same position, same speed => same step)
                continue
        return cnt


# no need to use stack, only care about length and top

        
            

        
