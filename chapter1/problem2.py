# install an external module use it to perform operation of your own

# text to speech 
# we install pyttsx3

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I am saba siddiqui im doing bca rn , i love to scroll phone lol i am very shy and beautifull no one can beat me on coding im pro ")
engine.runAndWait()