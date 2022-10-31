import random

# Welcome Section


print('******************\n\nPeter Answers\n\n******************')

print('Welcome to Peter Answers...\n')

print('Do you need to ask a question? Are you looking for answers?\nPeter offers you a space to ask anything you want. However, before each question you must write a petition. \n If the answer is not what you expected, at least you make catharsis and ask again.\n\n**')


# Petition to ask Question

petition = input('Petition > ')

if 'Peter, Please answer' not in petition and 'Peter, Please answer this question' not in petition:
    
    print('\nInvalid Petition!')
    
    print('You must request Peter to answer you your question')

else:
    
    question = input('Question > ')
    
    if len(question) == 0:
        
        print('\nPlease enter a valid question!')
        
    else:
        
        
        messages = [
            
                    "You shall not doubt of me at all, keep trusting on me and soon I'll answer.",
                    
                    "Your soul is too deep for me to find",
                    
                    "No more questions, getting sleepy.",
                    
                    "Don't you have a more interesting question?",
                    
                    "Soon you will know what you are looking for. At any time a sign will appear.",
                    
                    "Do you believe in me?",
                    
                    "I'm not answering that question.",
                    
                    "You must be a true believer for me to answer.",
                    
                    "I think only you know the answer to that question.",
                    
                    "We're not spiritually connected enough to answer this question."     
                    
                    ]
        
        new_messages = random.choice(messages)
        
        print('******Answer******\n\n')
        print(new_messages)
        
        
        
        
        
        
        
