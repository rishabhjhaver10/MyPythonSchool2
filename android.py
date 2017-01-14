from bs4 import BeautifulSoup
import json
import os
#path
folder = 'C:/Users/risha/Downloads/data/'

#dictionaries to store results to be stored in a json file finally
final = dict()
main = dict()
sub = dict()

#lists to store data for visualizaiton
dates = []
ratings_avg = []
ratings_total = []
ratings_1 = []
ratings_2 = []
ratings_3 = []
ratings_4 = []
ratings_5 = []
file_sizes = []
outfile = open('data_andriod_.json', 'w')
#looping through every folder, directory and file
for dirname, dirs, files in os.walk(folder):    
    for filename in files:
        #filename_without_extension, extension = os.path.splitext(filename)
        if 'android' in filename:
            #creating a beautifule soup object
            soup = BeautifulSoup(open(dirname+'/'+filename), 'lxml')
            print dirname+'/'+filename
            #using try-except statement to account for the missing values in the dataset
            try:
                avg_rating = soup.find('div', {'class' : 'score'})
            #print avg_rating
            #print avg_rating.get_text()
                ratings_avg.append([dirname.split('/')[5],float(avg_rating.get_text())])
            except:
                continue
            try:
                total_rating = soup.find('div', {'class' : 'reviews-stats'})
                x = total_rating.get_text()
                y = x.split()[0]
                #print y
                ratings_total.append([dirname.split('/')[5],int(y.replace(',',''))])
            except:
                continue
            
            try:
                rating = soup.find_all('span', {'class' : 'bar-number'})
                #print rating
                rating_5 = rating[0]
                ratings_5.append([dirname.split('/')[5],rating_5.get_text().replace(',','')])
                rating_4 = rating[1]
                ratings_4.append([dirname.split('/')[5],rating_4.get_text().replace(',','')])
                rating_3 = rating[2]
                ratings_3.append([dirname.split('/')[5],rating_3.get_text().replace(',','')])
                rating_2 = rating[3]
                ratings_2.append([dirname.split('/')[5],rating_2.get_text().replace(',','')])
                rating_1 = rating[4]
                ratings_1.append([dirname.split('/')[5],rating_1.get_text().replace(',','')])
            except:
                continue
            
            try:
                file_size = soup.find_all('div', {'class' : 'meta-info'})
                file_size1 = file_size[1]
                file_size2 = file_size1.get_text()
                file_size3 = str(file_size2.split()[1])
                file_size4 = int(filter(str.isdigit, file_size3))
                file_sizes.append([dirname.split('/')[5],int(file_size4)])
                version = file_size[3].get_text().split()[2]
            except:
                continue
            
            try:
                desc = soup.find('div', {'class' : 'show-more-content text-body'})
                description =  desc.get_text()
            except:
                continue
            #creating an intermediate dictionary
            sub = {'Rating_4': rating_4.get_text(), 'Rating_5': rating_5.get_text(), 
                   'Rating_2': rating_2.get_text(), 'Rating_3': rating_3.get_text(),
                   'Total_rating': y, 'Rating_1': rating_1.get_text(), 
                   'Average_rating' : avg_rating.get_text(), 'Version' : version,
                   'File_size' : file_size4, 'Description' : description }
            #the dictionary in required form
            main = {(dirname.split('/')[5] + '_' + filename.split('_')[0] + '_' + filename.split('_')[1]) : sub}
            final.update(main)
            
#dumping the dictionary in the json file            
json.dump(final, outfile)


#creating the required plots
import matplotlib.pyplot as plt
import numpy as np
import datetime
i1=[]
i2=[]
for i in file_sizes:
    i1.append(i[1])
    i2.append(datetime.datetime.strptime(i[0], "%Y-%m-%d"))
i3=[]
i4=[]
for i in ratings_avg:
    i3.append(i[1])
    i4.append(datetime.datetime.strptime(i[0], "%Y-%m-%d"))
i5=[]
i6=[]
for i in ratings_total:
    i5.append(i[1])
    i6.append(datetime.datetime.strptime(i[0], "%Y-%m-%d"))
i7=[]
i8=[]
for i in ratings_5:
    i7.append(i[1])
    i8.append(datetime.datetime.strptime(i[0], "%Y-%m-%d"))
i9=[]
i10=[]
for i in ratings_4:
    i9.append(i[1])
    i10.append(datetime.datetime.strptime(i[0], "%Y-%m-%d"))
i11=[]
i12=[]
for i in ratings_3:
    i11.append(i[1])
    i12.append(datetime.datetime.strptime(i[0], "%Y-%m-%d"))
i13=[]
i14=[]
for i in ratings_2:
    i13.append(i[1])
    i14.append(datetime.datetime.strptime(i[0], "%Y-%m-%d"))
i15=[]
i16=[]
for i in ratings_1:
    i15.append(i[1])
    i16.append(datetime.datetime.strptime(i[0], "%Y-%m-%d"))

figure1=plt.figure()
plt.plot(i2,i1,'o',label="Size")
figure1.figsave("Plot1_android.png")
plt.show()
figure2=plt.figure()
plt.plot(i4,i3,'o', label = 'Average Rating')
figure2.figsave("Plot2_android.png")
plt.show()
figure3=plt.figure()
plt.plot(i6,i5,'o', label = 'All Rating')
figure3.figsave("Plot3_android.png")
plt.show()
figure4=plt.figure()
plt.plot(i8,i7,'o', label = '5')
figure4.figsave("Plot4_android.png")
plt.show()
figure5=plt.figure()
plt.plot(i10,i9,'o', label = '4')
figure5.figsave("Plot5_android.png")
plt.show()
figure6=plt.figure()
plt.plot(i12,i11,'o', label = '3')
figure6.figsave("Plot6_android.png")
plt.show()
figure7=plt.figure()
plt.plot(i14,i13,'o', label = '2')
figure7.figsave("Plot7_android.png")
plt.show()
figure8=plt.figure()
plt.plot(i16,i15,'o', label = '1')
figure8.figsave("Plot8_android.png")
plt.show()
