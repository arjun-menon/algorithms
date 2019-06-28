class Solution:
    def query(self, src, dst, prev=None):
        if prev == None:
            prev = set()
        if (src, dst) in prev:
            return -1.0
        prev.add((src, dst))
        # print(src, dst, prev)
        if src not in self.qn or dst not in self.qn:
            return -1.0
        if src in self.qn:
            if dst in self.qn[src]:
                return self.qn[src][dst]
            for link in self.qn[src]:
                link_result = self.query(link, dst, prev)
                if link_result != -1.0:
                    return self.qn[src][link] * link_result
        return -1.0
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.qn = dict()
        for i in range(len(equations)):
            numerator = equations[i][0]
            denominator = equations[i][1]
            if not numerator in self.qn:
                self.qn[numerator] = dict()
            if not denominator in self.qn:
                self.qn[denominator] = dict()
            self.qn[numerator][denominator] = values[i]
            self.qn[denominator][numerator] = 1.0 / values[i]
        results = []
        for src, dst in queries:
            results.append(self.query(src, dst))
        return results
