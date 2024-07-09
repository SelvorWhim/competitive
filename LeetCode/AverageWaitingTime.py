class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sum_waiting_time = 0
        last_dish_finish_time = 0
        for arrival, time in customers:
            if last_dish_finish_time <= arrival:
                # chef is free when this customer arrives, starts cooking their dish immediately
                last_dish_finish_time = arrival + time
                sum_waiting_time += time
            else:
                # chef is busy, will get to this customer as soon as they finish the dishes in their queue - at last_dish_finish_time
                last_dish_finish_time += time
                sum_waiting_time += last_dish_finish_time - arrival
        return sum_waiting_time / len(customers)
