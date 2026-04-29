# lyrics to frequnecy convertor
def lyrics_to_freq(lyrics):
    mydict = {}
    for word in lyrics.split():
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1
    return mydict


def most_common_words(frequency):
    values = frequency.values()
    best = max(values)
    words = []
    for k in frequency:
        if frequency[k] == best:
            words.append(k)
    return (words, best)


def most_often(frequency, mintimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(frequency)
        if temp[1] >= mintimes:
            result.append(temp)
            for w in temp[0]:
                del frequency[w]
        else:
            done = True
    return result


lyrics = """You leapt from crumbling bridges, watching cityscapes turn to dust
Filming helicopters crashing in the ocean from way above
Got the music in you, baby, tell me why
Got the music in you, baby, tell me why
You've been locked in here forever, and you just can't say goodbye
Kisses on the foreheads of the lovers wrapped in your arms
You've been hiding them in hollowed-out pianos left in the dark
Got the music in you, baby, tell me why
Got the music in you, baby, tell me why
You've been locked in here forever, and you just can't say goodbye
Your lips, my lips
Apocalypse
Your lips, my lips
Apocalypse
Go and sneak us through the rivers
Flood is rising up on your knees
Oh, please
Come out and haunt me, I know you want me
Come out and haunt me
Sharing all your secrets with each other, since you were kids
Sleeping soundly with the locket that she gave you clutched in your fist
Got the music in you, baby, tell me why
Got the music in you, baby, tell me why
You've been locked in here forever, and you just can't say goodbye
You've been locked in here forever, and you just can't say goodbye
Oh, when you're all alone
I will reach for you
When you're feeling low
I will be there too"""

frequency = lyrics_to_freq(lyrics)
word = most_common_words(frequency)
print(word)
print(most_often(frequency, 5))

# took lyrics from google
