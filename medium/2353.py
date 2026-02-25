class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodInfo = {} # food -> (cuisine, rating)
        self.cuisineHeaps = {} # cuisine -> (- rating, food)

        for f, c, r in zip(foods, cuisines, ratings):
            self.foodInfo[f] = (c, r)

            if c not in self.cuisineHeaps:
                self.cuisineHeaps[c] = []

            heapq.heappush(self.cuisineHeaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foodInfo[food]
        self.foodInfo[food] = (cuisine, newRating)
        heapq.heappush(self.cuisineHeaps[cuisine], (-newRating, food))       

    def highestRated(self, cuisine: str) -> str:
        rating, food = self.cuisineHeaps[cuisine][0]
        while - rating != self.foodInfo[food][1]:
            heapq.heappop(self.cuisineHeaps[cuisine])
            rating, food = self.cuisineHeaps[cuisine][0]

        return food

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
