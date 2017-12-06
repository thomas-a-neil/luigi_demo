import luigi


class AddTask(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter()

    def run(self):
        print(self.x + self.y)
