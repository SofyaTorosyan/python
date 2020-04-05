import wikipedia
wiki_info = wikipedia.page("Yerevan") # get info about Yerevan
text = wiki_info.summary.split(". ")         #split string using .

def word_count_in_text(text):
    dict = {}
    for str in text:
        s = str.replace(',', ' ')
        words_in_text = s.split(" ")
        word_count = len(words_in_text)  
        dict[str] = word_count
    print("sentence - words count in sentence")
    for key, val in dict.items():    # key: = sentence   value : = words count
        print(key, val)
        print("\n")
    print("longest sentece length - count") 
    max_ = max(dict.values())
    max_count  = 0
    for i in dict.values():
        if i == max_:
            max_count += 1 
    print(max_, "     -    ", max_count)
        
word_count_in_text(text)


