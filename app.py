import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if  uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.insert(0, "Entire Chat")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.header(num_messages)
        with col2:
            st.header("Total Words")
            st.header(words)
        with col3:
            st.header("Media Shared")
            st.header(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.header(num_links)

        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values)
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)

        if selected_user == 'Entire Chat':
            st.title("Most Active User")
            new_df = helper.most_active_user(df)

            st.dataframe(new_df)
        
        st.title("Word Cloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
