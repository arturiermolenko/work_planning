class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            start_work_time: str,
            end_work_time: str,
            start_pause: str,
            end_pause: str
        ):
        self.name = name
        self.surname = surname
        self.start_work_time = start_work_time
        self.end_work_time = end_work_time
        self.start_pause = start_pause
        self.end_pause = end_pause
    
    def __str__(self):
        return f"{self.name} {self.surname}"

if __name__ == "__main__":
    artur = Worker(
        name = "Artur",
        surname = "Iermolenko",
        start_work_time = "06.30",
        end_work_time = "15.00",
        start_pause = "10.30",
        end_pause = "11.00"
    )
    print(artur)
