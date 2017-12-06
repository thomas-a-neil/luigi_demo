import luigi


class GenerateWords(luigi.Task):

    def output(self):
        return luigi.LocalTarget('lowercase.txt')

    def run(self):
        # write a dummy list of words to output file
        words = ['apple', 'banana', 'grapefruit']

        with self.output().open('w') as f:
            for word in words:
                f.write('{word}\n'.format(word=word))


class GenerateMoreWords(luigi.Task):

    def output(self):
        return luigi.LocalTarget('lowercase2.txt')

    def run(self):
        # write a dummy list of words to output file
        words = ['kiwi', 'mango', 'pineapple']

        with self.output().open('w') as f:
            for word in words:
                f.write('{word}\n'.format(word=word))


class CountLetters(luigi.Task):

    def requires(self):
        return GenerateWords(), GenerateMoreWords()

    def output(self):
        return luigi.LocalTarget('letter_counts.txt')

    def run(self):
        words = []
        for target in self.input():
            with target.open('r') as infile:
                words += infile.read().splitlines()

        # write each word to output file with its corresponding letter count
        with self.output().open('w') as outfile:
            for word in words:
                outfile.write('{word} | {letter_count}\n'.format(word=word, letter_count=len(word)))
