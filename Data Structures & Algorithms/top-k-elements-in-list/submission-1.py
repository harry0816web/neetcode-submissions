class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else: 
                freq_dict[num] += 1

        # .items(): turns each key-value pair -> tuple
        # key: function that sorted() used to sort, return item[1] means use value as sorted factor
        sorted_dict = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)

        return_arr = []
        for i in range(0, k):
            return_arr.append(sorted_dict[i][0])
        return return_arr