class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda i: i[1])

        count = 1

        bow = points[0][1]

        for start, end in points:
            if bow < start:
                bow = end
                count += 1
        