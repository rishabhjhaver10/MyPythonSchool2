from bs4 import BeautifulSoup
import json
import os

folder = 'C:/Users/risha/Downloads/data1/'
final = dict()
main = dict()
sub = dict()
dates = []
ratings_avg = []
ratings_total = []
ratings_1 = []
ratings_2 = []
ratings_3 = []
ratings_4 = []
ratings_5 = []
file_sizes = []
x = '_android'
outfile = open('data_andriod.json', 'w')
for dirname, dirs, files in os.walk(folder):
    for filename in files:
        filename_without_extension, extension = os.path.splitext(filename)
        if x in filename:
            soup = BeautifulSoup(open(dirname+'/'+filename), 'lxml')
            avg_rating = soup.find('div', {'class' : 'score'})
            #print avg_rating
            #print avg_rating.get_text()
            total_rating = soup.find('div', {'class' : 'reviews-stats'})
            x = total_rating.get_text()
            y = x.split()[0]
            #print y
            rating = soup.find_all('span', {'class' : 'bar-number'})
            #print rating
            rating_5 = rating[0]
            rating_4 = rating[1]
            rating_3 = rating[2]
            rating_2 = rating[3]
            rating_1 = rating[4]
            file_size = soup.find_all('div', {'class' : 'meta-info'})
            file_size1 = file_size[1]
            file_size2 = file_size1.get_text()
            file_size3 = str(file_size2.split()[1])
            file_size4 = int(filter(str.isdigit, file_size3))
            version = file_size[3].get_text().split()[2]
            desc = soup.find('div', {'class' : 'show-more-content text-body'})
            description =  desc.get_text()
            
            sub = {'Rating_4': rating_4.get_text(), 'Rating_5': rating_5.get_text(), 
                   'Rating_2': rating_2.get_text(), 'Rating_3': rating_3.get_text(),
                   'Total_rating': y, 'Rating_1': rating_1.get_text(), 
                   'Average_rating' : avg_rating.get_text(), 'Version' : version,
                   'File_size' : file_size4, 'Description' : description }
            main = {(dirname.split('/')[5] + '_' + filename.split('_')[0] + '_' + filename.split('_')[1]) : sub}
            final.update(main)
            json.dump(final, outfile)
            
            dates.append(str(dirname.split('/')[5]))
            ratings_avg.append(avg_rating.get_text())
            ratings_total.append(y)
            ratings_1.append(rating_1.get_text())
            ratings_2.append(rating_2.get_text())
            ratings_3.append(rating_3.get_text())
            ratings_4.append(rating_4.get_text())
            ratings_5.append(rating_5.get_text())
            file_sizes.append(file_size4)