class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        on_x = abs(sx - fx)
        on_y = abs(sy - fy)
        min_steps = 0

        if on_x <= on_y:
            min_steps += on_x + (on_y - on_x)
        else:
            min_steps += on_y + (on_x - on_y)

        if sx == fx and sy == fy:
            return t != 1

        return t >= min_steps