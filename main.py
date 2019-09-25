from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import operator



#getting names from user
name_of_person1 = input('Please enter the proper full name of person1: ') + ':' + ' ' 
name_of_person2 = input('Please enter the proper full name of person2: ') + ':' + ' ' 



#Loading the file and working with it.
with open('datasheet.txt', 'r', encoding="utf-8") as file:
  data = file.read().lower()
print(type(data))
print(data)
data = data.splitlines()


#for person1
person1 = []
#for loop to get the values
for i in range(1000000):


  try:
    person1.append(data[i].split(name_of_person1)[1].split('\n')[0])
    
  except:
    pass
person1_dummy = ''

#for person2
person2 = []
#for loop to get the values
for i in range(1000000):


  try:
    person2.append(data[i].split(name_of_person2)[1].split('\n')[0])
    
  except:
    pass
person2_dummy = ''

#making the text format for person1 and person2
for i in range(len(person1)):
  person1_dummy = str(person1_dummy) + ' ' + str(person1[i])
for i in range(len(person2)):
  person2_dummy = str(person2_dummy) + ' ' + str(person2[i])



#making the word cloud for person1
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', stopwords=["media", "omitted"], 
                min_font_size = 10).generate(person1_dummy) 
                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
print('Word cloud for ' + name_of_person1)
plt.show() 




#making the word cloud for person2
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', stopwords=["media", "omitted"], 
                min_font_size = 10).generate(person2_dummy) 
                       
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0)
print('Word cloud for ' + name_of_person2)
plt.show()   
