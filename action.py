import datetime
import speak
import webbrowser
import weather
import os




def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is Ai virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey harshad, How i can  help you !")  
        return "Hey harshad, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great harshad ") 
            return "I am doing great harshad" 
    
    elif "who devoloped you" in  data_btn :
            speak.speak("I devoloped by Harshad Tile, who developed me to assist with various tasks and provide information in a virtual assistant capacity." ) 
            return "I devoloped by Harshad Tile, who developed me to assist with various tasks and provide information in a virtual assistant capacity."  

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure harshad to stay with you")
           return "its my pleasure harshad to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning harshad i think you might need some help")
           return "Good morning harshad, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok harshad")
            return "ok harshad"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready  harshad , enjoy your music")                   
        return "gaana.com is now ready  harshad, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak(" ok harshad google open")  
        return "ok harshad google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("ok harshad YouTube open") 
        return "ok harshad YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("ok harshad songs playing...")
        return "ok harshad songs playing..." 

    else :
        speak.speak( "sorry harshad i'm able to understand!")
        return "sorry harshad i'm able to understand!"  




