import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
df = pd.read_csv(url)

# Convert datetime column
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

# App Title
st.title("🚲 Bike Ridership Analysis")

# Total Ridership Over Time
st.header("📈 Total Ridership Over Time")
fig, ax = plt.subplots()
ax.plot(df.index, df['cnt'], label="Total Ridership")
ax.set_xlabel("Date")
ax.set_ylabel("Ridership Count")
ax.set_title("Total Ridership Over Time")
ax.legend()
st.pyplot(fig)

# Ridership by Season
st.header("🌤️ Total Ridership by Season")
season_ridership = df.groupby('season')['cnt'].sum()
season_labels = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
season_ridership.index = season_ridership.index.map(season_labels)
fig, ax = plt.subplots()
season_ridership.plot(kind='bar', ax=ax)
ax.set_xlabel("Season")
ax.set_ylabel("Total Ridership")
ax.set_title("Total Ridership by Season")
st.pyplot(fig)

# Rolling Average
st.header("📊 Rolling Average of Total Ridership")
option = st.radio("Choose an option:", ('7-day average', '14-day average', 'Total ridership by week'))

if option == '7-day average':
    df['7_day_avg'] = df['cnt'].rolling(7).mean()
    fig, ax = plt.subplots()
    ax.plot(df.index, df['7_day_avg'], label="7-Day Average", color='orange')
    ax.set_title("7-Day Rolling Average")
    ax.legend()
    st.pyplot(fig)

elif option == '14-day average':
    df['14_day_avg'] = df['cnt'].rolling(14).mean()
    fig, ax = plt.subplots()
    ax.plot(df.index, df['14_day_avg'], label="14-Day Average", color='green')
    ax.set_title("14-Day Rolling Average")
    ax.legend()
    st.pyplot(fig)

else:
    df_weekly = df.resample('W').sum()
    fig, ax = plt.subplots()
    ax.plot(df_weekly.index, df_weekly['cnt'], label="Weekly Total", color='red')
    ax.set_title("Total Ridership by Week")
    ax.legend()
    st.pyplot(fig)

st.write("✅ Explore the visualizations above!")
