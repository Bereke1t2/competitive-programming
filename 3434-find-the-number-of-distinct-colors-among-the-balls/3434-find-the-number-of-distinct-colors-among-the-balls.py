class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colored = 0
        color_ball= defaultdict(int)
        ball_color = defaultdict(set)
        res = []
        for ball , color in queries:
            if ball in ball_color:
                color_ball[ball_color[ball]] -=1
                if color_ball[ball_color[ball]]==0:
                    del color_ball[ball_color[ball]]
                    colored -=1
            if not color in color_ball:
                colored +=1
            color_ball[color] +=1
            ball_color[ball] = color
            res.append(colored)
        return res
            

