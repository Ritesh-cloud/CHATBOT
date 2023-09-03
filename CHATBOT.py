#!/usr/bin/env python
# coding: utf-8

# In[10]:


total = [list(range(11))]
total
total = [list(range(12))]
total


# In[11]:


total = [list(range(11, 32))]
total


# In[12]:


total = [list(range(100))]
total


# In[15]:


total = [list(range(12))]
total


# In[19]:


tuple1 = [list(range(11)), list(range(12, 21)), list(range(22, 32))]
tuple1


# In[22]:


total = [list(range(53)), list(range(60)), list(range(70))]
total


# In[31]:


tuple3 = [list(range(12)), list(range(13, 23)), list(range(24, 35))]
tuple3


# In[51]:


import random 

input_user = [
    "ritesh",
    "dhoni",
    "football",
    "sachine",
    "virat",
    "goobye"
]

response_bot = [
    "bit mesra",
    "captain",
    "neymar",
    "goat",
    "run machine",
    "bye"
]

def generate_response(input_user):
    generate_response = radient.choise()
    
    if "ritesh" in user_input:
        return bot_response[0]
    
    elif "dhoni" in user_input:
        return bot_response[1]
    
    elif "footabll" in user_input:
        return bot_response[2]
    
    elif "sachine" in user_input:
        return bot_response[3]
    
    elif "virat" in user_input:
        return bot_response[4]
    
    elif "goodbye" in user_input:
        return bot_response[5]
    
    else:
        return "sorry i don't understand."
    
    while True:
    # Get user input
        user_input = input("User: ")

        # Generate and display bot response
        bot_response = generate_response(user_input)
        print("Bot:", bot_response)

        # Check if user wants to exit the program
        if "goodbye" in user_input:
            break
    


# In[6]:


import random 

input_user = [
    "ritesh",
    "dhoni",
    "football",
    "sachine",
    "virat", 
    "goodbye"
]

response_bot = [
    "bit mesra",
    "captain",
    "neymar",
    "goat",
    "run machine"
    "have a nice day"
]
#define function
def generate_response(input_user):
    generate_response = radient.choise()
    
    #user input response
    if "ritesh" in user_input:
        return bot_response[0]
    
    elif "dhoni" in user_input:
        return bot_response[1]
    
    elif "footabll" in user_input:
        return bot_response[2]
    
    elif "sachine" in user_input:
        return bot_response[3]
    
    elif "virat" in user_input:
        return bot_response[4]
    
    elif "goodbye" in user_input:
        return bot_response[5]
    
    else:
        return "sorry i don't understand."
    
    while True:
    # Get user input
        user_input = input("User: ")

        # Generate and display bot response
        bot_response = generate_response(user_input)
        print("Bot:", bot_response)

        # Check if user wants to exit the program
        if "goodbye" in user_input:
            break
    


# In[3]:


import random 

input_user = [
    "ritesh",
    "dhoni",
    "football",
    "sachine",
    "virat", 
    "goodbye"
]

response_bot = [
    "bit mesra",
    "captain",
    "neymar",
    "goat",
    "run machine"
    "have a nice day"
]
#define function
def generate_response(input_user):
    generate_response = radient.choise()
    
    #user input response
    if "ritesh" in user_input:
        return bot_response[0]
    
    elif "dhoni" in user_input:
        return bot_response[1]
    
    elif "footabll" in user_input:
        return bot_response[2]
    
    elif "sachine" in user_input:
        return bot_response[3]
    
    elif "virat" in user_input:
        return bot_response[4]
    
    elif "goodbye" in user_input:
        return bot_response[5]
    
    else:
        return "sorry i don't understand."
    
while True:
    # Get user input
    user_input = input("User: ")

    # Check if user wants to exit the program
    if "goodbye" in user_input:
        print("Bot: Goodbye! Exiting the program.")
        break

    # Generate and display bot response
    bot_response = generate_response(user_input)
    print("Bot:", bot_response)


# In[7]:


import random 

input_user = [
    "ritesh",
    "dhoni",
    "football",
    "sachine",
    "virat", 
    "goodbye"
]

response_bot = [
    "bit mesra",
    "captain",
    "neymar",
    "goat",
    "run machine"
    "have a nice day"
]
#define function
def generate_response(input_user):
    generate_response = radient.choise()
    
    #user input response
    if "ritesh" in user_input:
        return bot_response[0]
    
    elif "dhoni" in user_input:
        return bot_response[1]
    
    elif "footabll" in user_input:
        return bot_response[2]
    
    elif "sachine" in user_input:
        return bot_response[3]
    
    elif "virat" in user_input:
        return bot_response[4]
    
    elif "goodbye" in user_input:
        return bot_response[5]
    
    else:
        return "sorry i don't understand."
    
    while True:
    # Get user input
        user_input = input("User: ")

        # Generate and display bot response
        bot_response = generate_response(user_input)
        print("Bot:", bot_response)

        # Check if user wants to exit the program
        if "goodbye" in user_input:
            break
    

