class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        ban = []
        round_senate = list(senate)

        while len(set(round_senate)) != 1:
            next_senate = []
            for s in round_senate:
                if ban and ban[0] == s:
                    ban.pop(0)
                else:
                    if s == "R": ban.append("D")
                    else: ban.append("R")
                    next_senate.append(s)
            round_senate = next_senate

        if round_senate[0] == "R":
            return "Radiant"
        else:
            return "Dire"
        
# Solved 25m58s