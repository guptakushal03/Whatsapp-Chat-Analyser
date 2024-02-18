import re
import pandas as pd

def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s(?:AM|PM)\s-\s'
    
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    dates = [date.replace('\u202f', ' ') for date in dates]

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format="%m/%d/%y, %I:%M %p - ")
    df['message_date'] = df['message_date'].dt.strftime("%Y-%m-%d %H:%M")
    df.rename(columns={'message_date': 'date'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(':\s+', message, maxsplit=1)  # Use maxsplit=1 to split only at the first occurrence of ':'
        if len(entry) > 1:
            users.append(entry[0])
            messages.append(entry[1])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df