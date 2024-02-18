# WhatsApp Chat Analyzer

WhatsApp Chat Analyzer is a tool built with Python and Streamlit that allows users to analyze their WhatsApp chat data. It provides insights such as total messages, word count, media shared, links shared, monthly activity timeline, most active users, activity maps, and word clouds.

## Features

- **File Upload**: Users can upload their WhatsApp chat data in text format.
- **User Selection**: Users can choose to analyze the entire chat or select a specific user.
- **Analysis**: The application provides various analyses such as total messages, word count, media shared, links shared, monthly activity timeline, most active users, activity maps, and word clouds.
- **Visualization**: Results are visualized using interactive plots and charts.
- **Insights**: Users can gain insights into their chat behavior and patterns.

## Usage

1. **Install Dependencies**: Ensure you have Python and required dependencies installed. You can install dependencies using `pip install -r requirements.txt`.
2. **Run the Application**: Run the Streamlit application using `streamlit run app.py`.
3. **Upload Data**: Upload your WhatsApp chat data file in text format.
4. **Select Analysis**: Choose the analysis you want to perform and select the user (optional).
5. **View Results**: Explore the insights and visualizations generated based on your WhatsApp chat data.

## File Structure

- `app.py`: Main Python script containing the Streamlit application code.
- `preprocessor.py`: Module for data preprocessing tasks such as parsing dates and splitting messages.
- `helper.py`: Module containing helper functions for data analysis and visualization.
- `requirements.txt`: File containing required Python dependencies.
- `README.md`: This file containing information about the project.

## Dependencies

- Python 3.x
- Streamlit
- Pandas
- Matplotlib
- Urlextract
- Wordcloud

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or feature requests, please open an issue or submit a pull request.
