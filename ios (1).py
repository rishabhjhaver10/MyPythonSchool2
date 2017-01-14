import os
import json
from bs4 import BeautifulSoup

folder = 'C:/Users/risha/Downloads/data1/'
final = dict()
main = dict()
sub = dict()
ratings_current = []
ratings_all = []
sizes = []
dates = []
x = '_ios'
outfile = open('data_ios.json', 'w')
for dirname, dirs, files in os.walk(folder):
    for filename in files:
        filename_without_extension, extension = os.path.splitext(filename)
        if x in filename:
            soup = BeautifulSoup(open(dirname+'/'+filename), 'lxml')
            rating = soup.find_all('span', {'class' : 'rating-count'})
            total_rating_current_version = rating[0]
            rating_current = total_rating_current_version.get_text()
            total_rating = rating[1]
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
            sizes.append([int(file_size), date)
            ratings_current.append(rating_current)
            ratings_all.append(rating_all)
            final.update(main)
            #print main
json.dump(final, outfile)            



'''import matplotlib.pyplot as plt
import numpy as np
       
plt.plot(dates,file_size, label = 'FileSize')
plt.plot(dates, ratings_current, label = 'Current Version')
plt.plot(dates, ratings_all, label = 'All Version')
plt.show()'''

