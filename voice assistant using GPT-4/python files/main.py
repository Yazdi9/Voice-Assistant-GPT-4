import openai 
import pyttsx3
import speech_recognition as sr 
import random 

#set  OpenAI Key 
openai.api_key='Your_API_KEY'
model_id='gpt-3.5-turbo'

#Initialize the Text-To-Speech Engine
engine=pyttsx3.init() 

#change speech rate 
engine.setProperty('rate',100)

#get the variable voice 
voices=engine.getProperty('voices')

#choose a voice based on the voice id 
engine.setProperty('voice',voices[1].id)

#counter just for interacting purpose 
interaction_counter=0

def transcribe_audio_to_text(filename):
    
    recognizer=sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio=recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            print("")
            
def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    api_usage = response['usage']
    print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation
 
def speak_text(text):
    engine.say(text) 
    engine.runAndWait()
 
#starting conversation 

# Starting conversation
conversation = []
conversation.append({'role': 'user', 'content': 'chat with me as you be Friday AI from Iron Man, please make a one sentence phrase introducing yourself without saying something that sounds like this chat its already started'})
conversation = ChatGPT_conversation(conversation)
print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
speak_text(conversation[-1]['content'].strip())
 
def activate_assistant():
    starting_chat_pharses=['Yes Sir , how may I assist you ?',"Yes What can I do for you ?","how can I help you Sir?","Friday here, how can I help you today ?"
                           
                           "yes , what can I do for you today ?"
                           "yes sir , what's on your mind ?" ,
                           "Friday ready to assist  , what can I do for you ?" ,
                           "At your command , sir , How may I help you today ?" ,
                           "At Your command , Sir . How may I help you today ? " ,
                           "Yes Sir . How may I be of assistance to you right now ? " ,
                           "Yes boss ,I'm here to help , what do you need from me ?" ,
                           "Yes I'm listening . What can I do for you , sir ? " ,
                           "How can I assist you today , sir ?" ,
                           "Yes Sir How can I make your day easier?" ,
                           "Yes boss , what's the plan ?" ,
                           "Yes what's on your mind , sir ?"
                           ] 
    
    continued_chat_pharase=["yes","yes","sir","boss","I'm all ears"]
    random_chat=""
    if(interaction_counter==1):
        random_chat=random.choice(starting_chat_pharses)
    else:
        random_chat=random.choice(continued_chat_pharase)
    return random_chat 

def append_to_log(text):
    with open("chat_log.txt","a")  as f :
        f.write(text+"\n")
        
while True: 
    print("say Friday to start ...")
    recognier=sr.Recognizer()
    with sr.Microphone() as source :
        audio=recognier.listen(source)
        try:
            transcribtion=recognier.recognize_google(audio)
            if "friday" in transcribtion.lower():
                interaction_counter +=1 
                filename="input.wav"
                
                readyToWork= activate_assistant()
                speak_text(readyToWork)
                print(readyToWork)
                recognier=sr.Recognizer()
                
                with sr.Microphone() as source :
                    source.pause_threshold=1 
                    audio=recognier.listen(source,pharse_time_limit=None,timeout=None)
                    with open(filename,"wb") as f :
                       f.write(audio.get_wav_data())
                
                text=transcribe_audio_to_text(filename) 
                
                if text :
                    
                    print(f"you said :{text}") 
                    append_to_log(f"You :{text}\n") 
                    
                    print(f"Friday says :{conversation}")
                    
                    prompt=text 
                    
                    conversation.append({'role':'user','content':'prompt'})
                    
                    conversation=ChatGPT_conversation(conversation)
                    
                    print('{0} :{1}\n'.format(conversation[-1]['role'].stripe(),conversation[-1])['content'])
                    
                    append_to_log(f"Friday :{conversation[-1]['content']}\n")
                    
                    speak_text(conversation[-1]['content'])
            
        except Exception as e :
            
            continue
                    
                    
                     
                        
                   
  
         
        
    


