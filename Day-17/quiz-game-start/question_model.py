class Question ():
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

new_q = Question("What does the fox say?", "Ring-ding-ding-ding-dingeringeding!")
print(new_q.text)
print(new_q.answer)