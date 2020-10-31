import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3

client = wolframalpha.Client("VGRH2A-VJ9W4JUJX6")
sg.theme('DarkBlack')   # Add a touch of color
text = sg.popup_get_text('Enter a command','PyAssistant')
engine = pyttsx3.init()
wiki_res=''
wolfram_res = ''
try:
        wiki_res = wikipedia.summary(text, sentences=2)
        wolfram_res = next(client.query(text).results).text
except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(text).results).text
except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(text).results).text
except:
        wiki_res = wikipedia.summary(text, sentences=2)

engine.say(str(wolfram_res)+str(wiki_res))
event = sg.PopupNonBlocking(text+'\n\n'+wolfram_res,"Wikipedia Result: "+wiki_res)
print(event)


# engine.say(str(wolfram_res)+str(wiki_res))
engine.runAndWait()
engine.stop()