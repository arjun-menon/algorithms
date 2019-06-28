class Solution:
    def nextClosestTime(self, time):
        digits = (int(time[0]), int(time[1]), int(time[3]), int(time[4]))
        check = lambda k: k[0] <= 2 and (k[1] <= 3 if k[0] == 2 else True) and k[2] <= 5
        valid_combos = sorted(filter(check, itertools.product(digits, repeat=4)))
        result = next(itertools.chain(filter(lambda k: k > digits, valid_combos), valid_combos))
        return "%d%d:%d%d" % (result[0], result[1], result[2], result[3])
