class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            start_work_time: str,
            end_work_time: str,
            start_pause: str,
            end_pause: str,
            cook_day: int | None = None
    ):
        self.name = name
        self.surname = surname
        self.start_work_time = start_work_time
        self.end_work_time = end_work_time
        self.start_pause = start_pause
        self.end_pause = end_pause
        self.cook_day = cook_day

    def __str__(self):
        return f"{self.name} {self.surname}"
