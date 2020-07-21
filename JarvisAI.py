import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak("Good Morning!")

	elif hour >= 12 and hour < 18:
		speak("Good Afternoon!")

	else:
		speak("Good Evening!")

	speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
	# It takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"user said: {query}\n")

	except sr.UnknownValueError:
		# print(e)
		speak('Sorry sir! I didn\'t get that! Try typing the command!')
		query=str(input('command: ')) 
		return "None"
	return query


if __name__ == "__main__":
	wishMe()
	while True:

		query = takeCommand().lower()

#executing tasks based on query
	if 'wikipedia' in query:
		speak('Searching Wikipedia....')
		query = query.replace("Wikipedia","")
		results = wikipedia.summary(query, sentences=2)
		print(results)
		speak(results)

	elif 'open youtube' in query:
		webbrowser.open("youtube.com")

	elif  'open google' in query:
		webbrowser.open("google.com")

	elif 'open W3school' in query:
		webbrowser.open("w3school.com")
		
	
	elif 'play music' in query:
		
		music.dir = 'C:\\Downloads\\Music\\01-Bad.Blood.feat.Kendrick.Lamar.mp3'
		songs = os.listdir(music_dir)
		#print(songs)
		os.startfile(os.path.join(music_dir),songs[0]) 