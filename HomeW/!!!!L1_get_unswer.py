welcome= input('say something? ')
def get_answer(question, answer):
    question = welcome
    answer  = {'Hi':'Hello',"How are u?":"Fine",'Good by':'See u later'}
    return answer[question]
print (get_answer)

#не работает((((