# # -*- coding: utf-8 -*-
""" Eliza homework. Relationship advisor """
__author__ = 'Tho Tran'

import random
import re

# %1 indicates the position to insert a text/char
# 2d list's length is 2: for each list at index 0 --> regex and index 1 --> responses
pattern_list = [
                [[r'[Mm]y name is \w'],
                ['Hello %1, how are you feeling today?', 
                'Hi %1, how are you feeling today?', 
                'Greeting %1, how are you feeling today?']],

                [[r'feel(ing)?.+(good|great|happy|joyful|well|ok)'], 
                ['That is good to hear, How is your family doing?',
                'Great! How is your family doing?',
                'Glad to hear it, How is your family doing?']],

                [[r'feel(ing)?.+(sad|saddened|angry|down|bad)'], 
                ['That is not good to hear, what happened?',
                'Why is that',
                'What happened?']],

                [[r'not\sfeel(ing)?.+(well|good|great|ok)'], 
                ['That is not good to hear, what happened?',
                'What happened?',
                'Something happened?']],

                [[r'([Tt]hey are|[Mm]y family).+(good|great|ok|well)'], 
                ['''That's wonderful, do you have any brother or sister?''', 
                'Wonderful! what does your family do for fun?',
                '''That's great, what type of food does your family usually eat?''']],

                [[r'I have.+brother'],
                ['How old is he?', 
                'Do you like hanging out with him?']],

                [[r'I have.+sister'],
                ['How old is she?', 
                'Do you like hanging out with her?']],

                [[r'I have.+brothers'],
                ['Which of your brothers do you like most?', 
                'Are you the youngest?']],

                [[r'I have.+sisters'],
                ['Which of your sisters do you like most?', 
                'Are you the youngest?']],

                [[r'[Mm]y\s(mom|dad)\s(likes|enjoys)\s(cooking|making)'],
                ['What else?',
                'This is making me hungry now. Do you want to get something to eat?']],

                [[r'[Mm]y family.+(eating|having)'],
                ['What else?',
                'Have they ever tried Taco Bell?',
                '''I'm hungry now. Would you like to go to Taco Bell''']],

                [[r'[Mm]y\sfamily\slikes.+\w|[Tt]hey\slike.+\w|[Ww]e\slike.+\w'],
                ['What else do you guys do for fun?',
                'What else do they like?',
                'That sounds fun, What else?',
                'What is there to like?',
                'Why do they like it?']],

                [[r"[Nn]o|\w.+not|\w.+haven't|\w.+hasn't"],
                ["Why not?",
                'What is the reason?',
                'How come?',
                'Ok, do you have any question for me?']],

                [[r'[Bb]ecause'],
                ['There has to be more',
                '''You're not lying to me, right?''']],

                [[r'[Yy]es|[Yy]ep'],
                ['Awesome, is there anything you would like to ask me?',
                'Nice, do you have any question for me?']],

                [[r'[Wwhat] are you|([Aa]re)?.*\w\smachine'],
                ['''I don't know, do you like machine?''',
                'Maybe I am, do you like machine?',
                'Do you like machine?']],

                [[r'[Ww]hat\w.+you like'],
                ['I like to play video games',
                'I like to play basketball']],

                [[r'video\sgame|game'],
                ['I like to play Lost Ark',
                'I like to play Halo',
                'I like to play Final Fantasy']],

                [[r'[Bb]asketball'],
                ["It's a fun sport",
                'I like to do step backs and shoot',
                'Do you like playing basketball']],

                [[r"[Ii]\s(don't like|hate|don't care|despise).+machine"],
                ['Bye']],

                [[r"[Ii]\s(love|like|).+machine"],
                ['We can be friend then, what would you like to ask me?',
                'Yay :)']],

                [[r'[Ii].+(had|lost|called|made|caused|got|\w)'],
                ['Wow, do you have any question for me?',
                'LOL, do you have any question for me',
                'Bee-Boo-Boo-Bop, do you have any question for me']],

                [[r'end'],
                ['When did it end?']],

                [[r'start'],
                ['When did it start?']]
                ]

def get_regexs(pattern_list):
    reg_list = []
    for i in range(0, len(pattern_list)):
        reg_list.append(pattern_list[i][0])
    return reg_list

def get_responses(pattern_list):
    resp_list = []
    for i in range(0, len(pattern_list)):
        resp_list.append(pattern_list[i][1])
    return resp_list

def translate(text):
    response = text
    subject_nouns = {'I':'You', "I'm":"You're", 'I am':"You're", 
                    'He':'He', 'She':'She', 'We':'You all', 'My':'Your'}
    text_split = text.split(" ")
    key_list = subject_nouns.keys()
    for word in text_split:
        for key in key_list:
            if str(word) == key:
                response = re.sub(word, subject_nouns[key], response)
            if str(word) == key.lower():
                response = re.sub(str(word).lower(), str(subject_nouns[key]).lower(), response)
    response = re.sub(r'ed', 'ing', response)
    return response

class Eliza:
    def __init__(self, pattern_list):
        self.regex = get_regexs(pattern_list)
        self.responses = get_responses(pattern_list)

    def respond(self, text):
        for i in range(0, len(self.regex)):
            if i == 0 and re.search(self.regex[i][0],text):
                text_split = text.split(" ")
                response = random.choice(self.responses[i])
                response = re.sub('%1', text_split[-1], response)
                return response
            if re.search(r'\w?ed', text):
                response = translate(text)
                return response
            if re.search(self.regex[i][0], text):
                response = random.choice(self.responses[i]) 
                return response
            
        return '''Sorry, I don't understand, could you rephrase it in a different way'''

def eliza_interface():
    print('-'*100)
    print('RULES\n')
    print('Please type in English') 
    print('Please type in complete sentences')
    print('Punctuation is not required at the end of the sentence')
    print('Type "Bye" to end the conversation')
    print('-'*100)
    print('Hello my name is Eliza')
    print('What is your name?')

    user_input = ''
    eliza = Eliza(pattern_list)

    while user_input != 'Bye':
        user_input = input('> ')
        if user_input == 'Bye':
            print('Have a good day')
            continue
        if str(eliza.respond(user_input)) == 'Bye':
            print('O_O' + '\n' + "I don't like you either")
            user_input = 'Bye'
            continue
        print(eliza.respond(user_input))

if __name__ == "__main__":
    eliza_interface()
