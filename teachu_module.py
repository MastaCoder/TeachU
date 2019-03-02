# Two question types: Questions based on information given in the text and
# questions based on keywords (For future continuation)
from textblob import TextBlob


NOUNS = ["NN", "NNS", "NNP", "NNPS", "PRP"]


# Class that maps each sentence into an object with different types of clauses
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.tags = sentence.tags
        # Current index position in words list
        self.pos = 0
        self.main_clause = []
        self.claux_list = []
        self.incr_value = 0
        self.process()

    # Y'all know how python testing is lmao
    def incr(self):
        self.incr_value += 1
        print(self.incr_value)

    # Gets current tag and returns False if done iterating
    def tag_iterate(self):
        try:
            tag = self.tags[self.pos]
            return tag
        except IndexError:
            return False

    # Main mapping method to check for various types of clauses (right now
    # only prepositions are accounted for)
    def process(self):
        while True:
            tag = self.tag_iterate()
            if not tag:
                return
            # IN is preposition wordtype
            if tag[1] == "IN":
                self.claux_list.append(self.claux())
                tag = self.tag_iterate()
            if not tag:
                return
            self.main_clause.append(tag)
            self.pos += 1

    # Coined from _Aux_iliary _Clau_se
    # Composed of preposition and incomplete clause
    def claux(self):
        claux = []
        end_check = False
        while True:
            tag = self.tag_iterate()
            if not tag:
                self.pos += 1
                return claux
            # Checks if two nouns occur in a row to break the claux
            # Usually this works but there are exceptions that I will work on
            if tag[1] in NOUNS:
                if end_check:
                    return claux
                end_check = True
            else:
                end_check = False
            claux.append(tag)
            self.pos += 1

    # Regurgitate sentence map
    def regurg(self):
        main_clause = ' '.join([word for word, pos in self.main_clause])
        print(f"Main Clause: {main_clause}")
        index = 1
        for claux in self.claux_list:
            claux = ' '.join([word for word, pos in claux])
            print(f"Claux {index}: {claux}")
            index += 1


# Parse sentences in string
def parse_sentences(string):
    txt = TextBlob(string)
    for sentence in txt.sentences:
        s_map = Sentence(sentence)
        s_map.regurg()


with open('notes2', encoding="utf8") as file:
    notes = file.read()

parse_sentences(notes)

