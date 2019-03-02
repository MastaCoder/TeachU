from textblob import TextBlob

def parsee(string):
    try:
        txt = TextBlob(string)
        all_questions = []
        # Each sentence is taken from the string input and passed to genQuestion() to generate questions.
        for sentence in txt.sentences:
            question = genQuestion(sentence)
            if question:
                all_questions.append(question)
        return all_questions

    except Exception as e:
        raise e


def genQuestion(line):
    if type(line) is str:  # If the passed variable is of type string.
        line = TextBlob(line)  # Create object of type textblob.blob.TextBlob

    bucket = {}  # Create an empty dictionary

    for i, j in enumerate(
            line.tags):  # line.tags are the parts-of-speach in English
        if j[1] not in bucket:
            bucket[
                j[1]] = i  # Add all tags to the dictionary or bucket variable

    if verbose:  # In verbose more print the key,values of dictionary
        print('\n', '-' * 20)
        print(line, '\n')
        print("TAGS:", line.tags, '\n')
        print(bucket)

    question = ''  # Create an empty string

    # Create a list of tag-combination

    l1 = ['NNP', 'VBG', 'VBZ', 'IN']
    l2 = ['NNP', 'VBG', 'VBZ']

    l3 = ['PRP', 'VBG', 'VBZ', 'IN']
    l4 = ['PRP', 'VBG', 'VBZ']
    l5 = ['PRP', 'VBG', 'VBD']
    l6 = ['NNP', 'VBG', 'VBD']
    l7 = ['NN', 'VBG', 'VBZ']

    l8 = ['NNP', 'VBZ', 'JJ']
    l9 = ['NNP', 'VBZ', 'NN']

    l10 = ['NNP', 'VBZ']
    l11 = ['PRP', 'VBZ']
    l12 = ['NNP', 'NN', 'IN']
    l13 = ['NN', 'VBZ']

    # With the use of conditional statements the dictionary is compared with the list created above

    if all(key in bucket for key in
           l1):  # 'NNP', 'VBG', 'VBZ', 'IN' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[
            bucket['NNP']] + ' ' + line.words[bucket['VBG']] + '?'

    elif all(key in bucket for key in l2):  # 'NNP', 'VBG', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[
            bucket['NNP']] + ' ' + line.words[bucket['VBG']] + '?'

    elif all(key in bucket for key in
             l3):  # 'PRP', 'VBG', 'VBZ', 'IN' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[
            bucket['PRP']] + ' ' + line.words[bucket['VBG']] + '?'

    elif all(key in bucket for key in l4):  # 'PRP', 'VBG', 'VBZ' in sentence.
        question = 'What ' + line.words[bucket['PRP']] + ' ' + ' does ' + \
                   line.words[bucket['VBG']] + ' ' + line.words[
                       bucket['VBG']] + '?'

    elif all(key in bucket for key in l7):  # 'NN', 'VBG', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[
            bucket['NN']] + ' ' + line.words[bucket['VBG']] + '?'

    elif all(key in bucket for key in l8):  # 'NNP', 'VBZ', 'JJ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[
            bucket['NNP']] + '?'

    elif all(key in bucket for key in l9):  # 'NNP', 'VBZ', 'NN' in sentence
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[
            bucket['NNP']] + '?'

    elif all(key in bucket for key in l11):  # 'PRP', 'VBZ' in sentence.
        if line.words[bucket['PRP']] in ['she', 'he']:
            question = 'What' + ' does ' + line.words[
                bucket['PRP']].lower() + ' ' + line.words[
                           bucket['VBZ']].singularize() + '?'

    elif all(key in bucket for key in l10):  # 'NNP', 'VBZ' in sentence.
        question = 'What' + ' does ' + line.words[bucket['NNP']] + ' ' + \
                   line.words[bucket['VBZ']].singularize() + '?'

    elif all(key in bucket for key in l13):  # 'NN', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[
            bucket['NN']] + '?'

    # When the tags are generated 's is split to ' and s. To overcome this issue.
    if 'VBZ' in bucket and line.words[bucket['VBZ']] == "’":
        question = question.replace(" ’ ", "'s ")

    # Print the genetated questions as output.
    return question

verbose = False
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        
    def do_POST(self):
        
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        response = BytesIO()
        #print(body.decode('utf-8'))
        response.write(b'{"0":""')
        count = 0
        for a in parsee(body.decode('utf-8')):
            count += 1
            response.write((',"' + str(count) + '":"').encode('utf-8'))
            response.write(a.encode('utf-8'))
            response.write(b'"')
        response.write(b'}')
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  
        self.end_headers()
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
