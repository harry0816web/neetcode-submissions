class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # class Height:
        #     def __init__(self, h, id):
        #         self.h = h
        #         self.id = id

        
        tiles = set()
        for h in heights:
            tiles.add(h)
        tiles = set(sorted(tiles))
        max_a = 0

        # print(tiles)
        for tile in tiles:
            max_width = 0
            width = 0
            # print("tile:", tile)
            for height in heights:
                # print("height: ", height)
                if height >= tile:
                    width += 1
                else:
                    width = 0
                max_width = max(max_width, width)
                    
            # print(max_width)
            max_a = max(max_width * tile, max_a)

        return max_a
        

        