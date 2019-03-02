from textblob import TextBlob

NOUNS = ["NN", "NNS", "NNP", "NNPS"
NNPS]

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.tags = sentence.tags
        self.pos = 0
        self.process()

    def process(self):
        while True:
            tag = self.tags[self.pos]
            if tag[1] == "IN":
                claux = self.claux()
                # auxillary clause haha get it

    def claux(self):
        claux_list = []
        end_check = False
        while True:
            tag = self.tags[self.pos]
            if tag[1] in NOUNS:
                if end_check:
                    return claux_list
                end_check = True
            else:
                end_check = False
            claux_list.append(tag)
            self.pos += 1


def parse_sentences(string):
    txt = TextBlob(string)
    for sentence in txt.sentences:
        s_map = Sentence(sentence)


with open('notes2', encoding="utf8") as file:
    notes = file.read()

parse_sentences(notes)

