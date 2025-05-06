import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset from the URL
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
df = pd.read_csv(url)

# Convert datetime to pandas datetime format
df['datetime'] = pd.to_datetime(df['datetime'])

# Set the datetime column as the index
df.set_index('datetime', inplace=True)

# Streamlit App Layout
st.title("Bike Ridership Analysis")

# Total Ridership Plot
st.header("Total Ridership Over Time")
fig, ax = plt.subplots()
ax.plot(df.index, df['cnt'], label="Total Ridership")
ax.set_xlabel("Date")
ax.set_ylabel("Ridership Count")
ax.set_title("Total Ridership Over Time")
ax.legend()
st.pyplot(fig)

# Total Ridership by Season
st.header("Total Ridership by Season")
season_ridership = df.groupby('season')['cnt'].sum()
season_labels = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
season_ridership.index = season_ridership.index.map(season_labels)
fig, ax = plt.subplots()
season_ridership.plot(kind='bar', ax=ax)
ax.set_xlabel("Season")
ax.set_ylabel("Total Ridership")
ax.set_title("Total Ridership by Season")
st.pyplot(fig)

# Rolling Average Selection
st.header("Rolling Average of Total Ridership")
rolling_option = st.radio(
    "Select Rolling Average Option:",
    ('7-day average', '14-day average', 'Total ridership by week')
)

# Calculate Rolling Averages or Resampling based on selection
if rolling_option == '7-day average':
    df['7_day_avg'] = df['cnt'].rolling(window=7).mean()
    fig, ax = plt.subplots()
    ax.plot(df.index, df['7_day_avg'], label="7-Day Rolling Average", color='orange')
    ax.set_xlabel("Date")
    ax.set_ylabel("Rolling Average Ridership")
    ax.set_title("7-Day Rolling Average of Total Ridership")
    ax.legend()
    st.pyplot(fig)

elif rolling_option == '14-day average':
    df['14_day_avg'] = df['cnt'].rolling(window=14).mean()
    fig, ax = plt.subplots()
    ax.plot(df.index, df['14_day_avg'], label="14-Day Rolling Average", color='green')
    ax.set_xlabel("Date")
    ax.set_ylabel("Rolling Average Ridership")
    ax.set_title("14-Day Rolling Average of Total Ridership")
    ax.legend()
    st.pyplot(fig)

elif rolling_option == 'Total ridership by week':
    df_weekly = df.resample('W').sum()
    fig, ax = plt.subplots()
    ax.plot(df_weekly.index, df_weekly['cnt'], label="Total Weekly Ridership", color='red')
    ax.set_xlabel("Week")
    ax.set_ylabel("Total Ridership")
    ax.set_title("Total Ridership by Week")
    ax.legend()
    st.pyplot(fig)

# Final note
st.write("Explore the visualizations above!")

