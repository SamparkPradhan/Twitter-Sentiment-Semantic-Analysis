import pandas as pd
import numpy as np

# Reading all the csv files into data frame.
# The csv should be in the same folder as i am giving relative lcoation to access them.
df1 = pd.read_csv('Search_Tweets.csv')
df2 = pd.read_csv('Stream_Tweets.csv')

# Merging the two data frames into one so that i can clean them.

df = pd.concat([df1, df2], ignore_index=True)

# Converting Tweet_Text and Tweet_Location into string type

df.Tweet_Location = df.Tweet_Location.apply(lambda x: str(x))
df.Tweet_Text =df.Tweet_Text.apply(lambda x: str(x))

# First I am removing unnecessary white spaces

df['Tweet_Text'] = df['Tweet_Text'].str.strip()

# Using regex to remove urls from Tweet_text column

df['Tweet_Text'] = df['Tweet_Text'].str.replace('http\S+|www.\S+', '', case=False)

# I am using a function to remove all other special character which are not in ASCII and do not have any significant
# meaning. This includes smiley's too


def remove_all_non_ascii(txt):
    return ''.join(i for i in txt if ord(i) < 128)


# Applying the function to Tweet_Text and Tweet_Location columns
df['Tweet_Text'] = df['Tweet_Text'].apply(remove_all_non_ascii)
df['Tweet_Location'] = df['Tweet_Location'].apply(remove_all_non_ascii)

# Exporting my cleaned tweets into another csv
# As the some locations were null they should be replaced by nan to indicate a empty value
# This file i am loading into mongodb
df.to_csv('all_cleaned_tweets.csv', sep=',', encoding='utf-8',index=False)

# As metadata is not required for word counts in pyspark I am only creating a csv with Tweet_text column
df.drop(columns=['Tweet_Time','Tweet_Location'], axis =1, inplace=True)
df.to_csv('cleaned_tweets.csv', sep=',', encoding='utf-8',index=False)