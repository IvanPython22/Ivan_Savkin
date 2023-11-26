class Computer:
    def __init__(self, cpu, raw, ssd, video_card):
        self.cpu = cpu
        self.ssd = ssd
        self.raw = raw
        self.video_card = video_card

    def __str__(self):
        details = f'CPU: {self.cpu}, SSD: {self.ssd}, RAW: {self.raw}, Video_card: {self.video_card}'
        return details


class Builder:
    def __init__(self):
        self.computer = Computer(None, None, None, None)

    def get_processor(self, cpu):
        self.computer.cpu = cpu
        return self

    def get_ssd(self, ssd):
        self.computer.ssd = ssd
        return self

    def get_raw(self, raw):
        self.computer.raw = raw
        return self

    def get_video_card(self, video_card):
        self.computer.video_card = video_card
        return self

    def build(self):
        return self.computer


builder = Builder()
my_computer = (builder.get_processor("Intel i7")
               .get_ssd("900GB")
               .get_raw("32GB")
               .get_video_card("RTX 3070")
               .build())

print(my_computer)