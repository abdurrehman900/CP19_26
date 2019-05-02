
# coding: utf-8

# In[ ]:


import speech_recognition as sr
 
r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Thank You!')
    
text = r.recognize_google(audio)
print (text)

