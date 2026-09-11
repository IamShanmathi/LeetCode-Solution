class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {}

        for i in range(len(list1)):
            index[list1[i]] = i

        min_sum = float('inf')
        result = []

        for j in range(len(list2)):
            if list2[j] in index:
                total = index[list2[j]] + j

                if total < min_sum:
                    min_sum = total
                    result = [list2[j]]

                elif total == min_sum:
                    result.append(list2[j])

        return result
        