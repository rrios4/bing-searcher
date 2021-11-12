from random_word import RandomWords
import webbrowser
import time

#initialize variables
r = RandomWords()
bingURL = 'https://www.bing.com/search?q='

#running loop from 0 to 30
for i in range(0,34):
    #open website
    webbrowser.open(bingURL + str(r.get_random_word()))
    #printing numbers
    print(i)
    #adding 2 seconds time delay
    time.sleep(5)