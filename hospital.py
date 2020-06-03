class Hospital():

    def occupied_fields(self, y_max, y_min, x_max, x_min):
        up_spaces = self.y
        count = 0
        while up_spaces <= y_max and count < self.range:
            self.reach.append((self.x, up_spaces))
            count += 1;


    def __init__(self, x, y, range, city):
        self.x = x
        self.y = y
        self.range = range
        self.reach = []
        y_max = min(y + range, city.height - 1)
        y_min = max(y - range, 0)
        x_max = min(x + range, city.width - 1)
        x_min = max(x - range, 0)
        up_spaces = self.y
        count = 0
        while up_spaces <= y_max and count <= self.range:
            self.reach.append((self.x, up_spaces))
            count += 1
            up_spaces += 1

        up_spaces = self.y
        count = self.range
        while up_spaces >= y_min and count >= 0:
            self.reach.append((self.x, up_spaces))
            count -= 1
            up_spaces -= 1

        side_spaces = self.x
        count = 0
        while side_spaces <= x_max and count <= self.range:
            self.reach.append((side_spaces, self.y))
            count += 1
            side_spaces += 1

        side_spaces = self.x
        count = self.range
        while side_spaces >= x_min and count >= 0:
            self.reach.append((side_spaces, self.y))
            count -= 1
            side_spaces -= 1

        self.reach = list(dict.fromkeys(self.reach))


