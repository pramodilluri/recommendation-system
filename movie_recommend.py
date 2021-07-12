#!/usr/local/bin/python3.9

print("============ Movie Recommendation System ===============")

import pandas

def sort_by_agebucket():

    age_bucket_recs = [{}, {}, {}]
    for i in sorted(age_rec.keys()):
        if i <= agebuckets[0]:
            if age_bucket_recs[0]:
                dict = age_bucket_recs[0]
            else:
                dict = {}
            for j in sorted(age_rec.get(i), reverse = True):
                if j <= 2:
                    break
                if dict.get(j):
                    dict[j].extend(age_rec.get(i).get(j))
                else:
                    dict[j] = age_rec.get(i).get(j)

            age_bucket_recs[0] = dict

        if i > agebuckets[0] and i <= agebuckets[1]:
            if age_bucket_recs[1]:
                dict = age_bucket_recs[1]
            else:
                dict = {}
            for j in sorted(age_rec.get(i), reverse = True):
                if j <= 2:
                    break;
                if dict.get(j):
                    dict[j].extend(age_rec.get(i).get(j))
                else:
                    dict[j] = age_rec.get(i).get(j)

            age_bucket_recs[1] = dict


        if i > agebuckets[1] and i <= agebuckets[2]:
            if age_bucket_recs[2]:
                dict = age_bucket_recs[2]
            else:
                dict = {}
            for j in sorted(age_rec.get(i), reverse = True):
                if j <= 2:
                    break;
                if dict.get(j):
                    dict[j].extend(age_rec.get(i).get(j))
                else:
                    dict[j] = age_rec.get(i).get(j)

            age_bucket_recs[2] = dict


        if i > agebuckets[2]:
            if age_bucket_recs[3]:
                dict = age_bucket_recs[3]
            else:
                dict = {}
            for j in sorted(age_rec.get(i), reverse = True):
                if j <= 2:
                    break;
                if dict.get(j):
                    dict[j].extend(age_rec.get(i).get(j))
                else:
                    dict[j] = age_rec.get(i).get(j)

            age_bucket_recs[3] = dict

    return age_bucket_recs


def find_age_bucket(age):
    if age <= agebuckets[0]:
        return 0
    if age > agebuckets[0] and age <= agebuckets[1]:
        return 1
    if age > agebuckets[1] and age <= agebuckets[2]:
        return 2
    if age > agebuckets[2]:
        return 3


def recommend_movies(age, max):
 
    recs = []
    rating_list = age_rec.get(age)

    # if direct match of age - Apt recommendation either <= 
    count = 0
    if rating_list:
        for i in range(5,2,-1):
            if rating_list.get(i) and count < max:
                for item in rating_list.get(i):
                    recs.append(item)
                    count += 1
                    if count == max :
                        break
    else:
    # if no direct match - pick best from age bucket
        age_group = find_age_bucket(age) 

        rating_list = age_bucket_recs[age_group]
        for i in range(5,2,-1):
            if rating_list.get(i) and count < max:
                for item in rating_list.get(i):
                    recs.append(item)
                    count += 1
                    if count == max :
                        break 

    # if recs not found - empty recommendation.
    return recs



## Main program sequence

df = pandas.read_csv('RatingsInput.csv')

agebuckets = [18, 35, 50]
age_rec = {}
dict = {}

index=0
for i in df['MovieName']:
    [id, name] = i.split(',')
    df['MovieID'][index] = id
    df['MovieName'][index] = name
    index+=1 


df.to_csv('RatingsInput_stage_1.csv')


index = 0
for i in df['MovieName']:
    df['MovieName'][index] = df['MovieName'][index].title()
    index += 1

df.to_csv('RatingsInput_stage_2.csv')


index = 0
for item in df['UserAge']:
    if not age_rec.get(item):
        age_rec[item] = {}

    rating = df['Rating'][index]
    if not age_rec[item].get(rating):
        age_rec[item][rating] = []
    
    age_rec[item][rating].append(df['MovieName'][index])

    index += 1


age_bucket_recs = sort_by_agebucket()

# find recommendation for new user list
df = pandas.read_csv('NewUsers.csv')

index = 0
for item in df['UserAge']:
    recs = recommend_movies(item, df['NoOfMoviesToRecommend'][index])
    df['Movies'][index] = recs
    index += 1

df.to_csv('Recommendation_output.csv')
