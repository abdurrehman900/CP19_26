import speech_recognition as sr
r = sr.recognizer()
with sr.Microphone() as source:
    print("SAY SOMETHING");
    audio = r.listen (source)
    print ("TIME OVER, THANKS")
    
try:
  print("TEXT: " + r.recognize_google(audio));
except:
  pass;