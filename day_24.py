#iterating over a tuple
def get_data(atuple):
    nums=()
    words=()
    for t in atuple:
        nums=nums + (t[0],)
        if t[1] not in atuple:
            words=words+(t[1],)
    min_n=min(atuple)
    max_n=max(atuple)
    unique_word= len(words)
    return(min_n,max_n,unique_word)

tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"),
          (2010,"Taylor"),
          (2008,"Joe"))
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year,"Taylor Swift wrote songs about", num_people, "people!")
