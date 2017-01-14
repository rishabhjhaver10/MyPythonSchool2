import os
import json
from bs4 import BeautifulSoup
#import matplotlib.pyplot as plt

#import numpy as np
#import datetime
#path 
folder = 'C:/Users/risha/Downloads/data/'

#dictionaries to store the results to be stores in json files
final = dict()
main = dict()
sub = dict()

#lists to store data for visualization
ratings_current = []
ratings_all = []
sizes = []
dates = []
x = '_ios'
outfile = open('data_ios_.json', 'w')
#looping through every folder, directory and file
for dirname, dirs, files in os.walk(folder):    
    for filename in files:
        filename_without_extension, extension = os.path.splitext(filename)
        if x in filename:
            #creating a beautiful soup object
            soup = BeautifulSoup(open(dirname+'/'+filename), 'lxml')
            print dirname+'/'+filename
            rating = soup.find_all('span', {'class' : 'rating-count'})
            #using the if-else statement to use the previous values incase of missing values
            if(len(rating)>1):
                total_rating_current_version = rating[0]
                rating_current = total_rating_current_version.get_text()
                total_rating = rating[1]
                rating_all = total_rating.get_text()
            else:
                total_rating = rating[0]
                rating_all = total_rating.get_text()
            version = soup.find('span', {'itemprop' : 'softwareVersion'})
            version1 = version.get_text()
            description = soup.find('p', {'itemprop' : 'description'})
            desc = description.getText()
            size = soup.find_all('li')
            size1 = size[21]
            size2 = size1.get_text()
            file_size = str(size2.split()[1])
            sub = {'version' : version1, 'description' : desc, 'total_rating' : rating_all, 'total_rating_current_version' : rating_current}
            main = {(dirname.split('/')[5] + '_' + filename.split('_')[0] + '_' + filename.split('_')[1]) : sub}
            #json.dump(main, outfile)
            dates.append(str(dirname.split('/')[5]))
            sizes.append([int(file_size), str(dirname.split('/')[5])])
            ratings_current.append([int(rating_current.split()[0]),str(dirname.split('/')[5])])
            ratings_all.append([int(rating_all.split()[0]),str(dirname.split('/')[5])])
            final.update(main)
            #print main
#dumping the dictionary in the json file            
json.dump(final, outfile)            



#creating plots for data visualization
i1=[]
i2=[]
for i in sizes:
    i1.append(i[0])
    i2.append(datetime.datetime.strptime(i[1], "%Y-%m-%d"))
i3=[]
i4=[]
for i in ratings_current:
    i3.append(i[0])
    i4.append(datetime.datetime.strptime(i[1], "%Y-%m-%d"))
i5=[]
i6=[]
for i in ratings_all:
    i5.append(i[0])
    i6.append(datetime.datetime.strptime(i[1], "%Y-%m-%d"))
figure1=plt.figure()
plt.plot(i2,i1,'o',label="Size")
figure1.figsave("Plot1_ios.png")
plt.show()
figure2=plt.figure()
plt.plot(i4,i3,'o', label = 'Current Version')
figure2.figsave("Plot2_ios.png")
plt.show()
figure3=plt.figure()
plt.plot(i6,i5,'o', label = 'All Version')
figure3.figsave("Plot3_ios.png")
plt.show()'''

