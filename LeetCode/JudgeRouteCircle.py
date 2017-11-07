class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        xPos,yPos = 0,0
        xMap = {'R':1,'L':-1}
        yMap = {'U':1,'D':-1}
        for step in moves:
            xPos += xMap.get(step,0) # default value 0
            yPos += yMap.get(step,0)
        return xPos == 0 and yPos == 0