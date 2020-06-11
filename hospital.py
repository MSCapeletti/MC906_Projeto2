def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def calculate_reach(tuple):
    x = tuple[0]
    y = tuple[1]
    d = tuple[2]
    city = tuple[3]
    reach = []
    xDist = d
    while xDist >= 0:
        yDist = d - xDist

        i = max(x - xDist, 0)
        while i <= min(x + xDist, city.width -1):
            j = max(y - yDist, 0)
            while j <= min(y + yDist, city.height -1):
                reach.append((i, j))
                j = j + 1

            i = i + 1

        xDist = xDist - 1

    return set(reach)

class Hospital():

    def __init__(self, x, y, range, city, reach=None):
        self.x = x
        self.y = y
        self.range = range
        self.city = city
        if reach == None:
            self.reach = []
            self.update_reach()
        else:
            self.reach = reach

    def copy(self):
        return Hospital(self.x, self.y, self.range, self.city, self.reach)

    #A lista retornada pode ser modificada sem afetar o hospital
    def get_reach(self):
        return self.reach

    def update_position(self, x, y):
        if x != self.x and y != self.y:
            self.x = x
            self.y = y
            self.update_reach()

    def update_range(self, range):
        if range != self.range:
            self.range = range
            self.update_reach()

    def update(self, x, y, range):
        if x != self.x and y != self.y and range != self.range:
            self.x = x
            self.y = y
            self.range = range
            self.update_reach()

    #Atualiza a lista de posições atendidas pelo hospital usando distância manhattan
    def update_reach(self):
        self.reach = calculate_reach((self.x, self.y, self.range, self.city))

        
