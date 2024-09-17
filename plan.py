from datetime import datetime
from typing import List
from worker import Worker


class Plan:
    def __init__(self, date: str, workers_list: List[Worker]):
        self.date = datetime.strptime(date, "%d-%m-%Y")
        self.workers_list = workers_list
        self.cook = self.get_cook()

    def print_plan(self):
        print(
            f'''
            Today {self.cook} is cooking.
            '''
        )

    def get_cook(self):
        for worker in self.workers_list:
            if worker.cook_day == (self.date.weekday() + 1):
                return worker


if __name__ == "__main__":
    artur = Worker(
        name="Artur",
        surname="Iermolenko",
        start_work_time="06.30",
        end_work_time="15.00",
        start_pause="10.30",
        end_pause="11.00",
        cook_day=1
    )
    plan = Plan(
        date="16-09-2024",
        workers_list=[artur]
    )
    plan.print_plan()