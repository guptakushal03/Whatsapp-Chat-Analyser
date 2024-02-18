from urlextract import URLExtract
from wordcloud import WordCloud
extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != "Entire Chat":
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    
    words = []
    for message in df['message']:
        words.extend(message.split())
    
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

def most_active_user(df):
    df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'Name', 'user': 'Percent'})
    return df

def create_wordcloud(selected_user, df):
    if selected_user != "Entire Chat":
        df = df[df['user'] == selected_user]
    
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def monthly_timeline(selected_user, df):
    if selected_user != "Entire Chat":
        df = df[df['user'] == selected_user]
    
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def week_activity_map(selected_user, df):
    if selected_user != "Entire Chat":
        df = df[df['user'] == selected_user]
    
    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != "Entire Chat":
        df = df[df['user'] == selected_user]
    
    return df['month'].value_counts()