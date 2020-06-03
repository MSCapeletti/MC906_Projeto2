class Hospital():

    def __init__(self, x, y, range, city):
        self.x = x
        self.y = y
        self.range = range
        self.city = city
        self.reach = []
        self.update_reach()

    #A lista retornada pode ser modificada sem afetar o hospital
    def get_reach(self):
        return self.reach.copy()

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.update_reach()

    #Atualiza a lista de posições atendidas pelo hospital usando distância manhattan
    def update_reach(self):
        self.reach = []
        d = self.range
        x = self.x
        y = self.y
        city = self.city

        xDist = d
        while xDist >= 0:
            yDist = d - xDist

            i = max(x - xDist, 0)
            while i <= min(x + xDist, city.width -1):
                j = max(y - yDist, 0)
                while j <= min(y + yDist, city.height -1):
                    self.reach.append((i, j))
                    j = j + 1

                i = i + 1

            xDist = xDist - 1

        self.reach = set(self.reach)
        


