import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

# Set page configuration to wide mode
st.set_page_config(layout="wide")

# Load the dataset
data = pd.read_csv('updated_data.csv')

# Title of the app
st.title('Car Sales Data Insights')

# Sidebar for navigation using menu
with st.sidebar:
    st.title('Navigation')
    selected = option_menu(
        menu_title=None,
        options=['Overview', 'Expected Sales', 'Yearly Data'],
        icons=['house', 'bar-chart', 'calendar'],
        menu_icon='cast',
        default_index=0,
        orientation='vertical'
    )

# Function to display overview section
def show_overview():
    st.subheader('Overview')
    
    with st.container():
        col1, col2 = st.columns(2)  # Create two columns for layout
        
        with col1:
              # 10 most expensive cars
            st.subheader('10 Most Expensive Cars')
            top_10_expensive = data.nlargest(10, 'Final_Price')
            st.write(top_10_expensive)
            # Vehicle counts by fuel
            st.subheader('Vehicle Counts by Fuel Type')
            fuel_counts = data['Fuel'].value_counts().reset_index()
            fuel_counts.columns = ['Fuel', 'Count']
            st.bar_chart(fuel_counts.set_index('Fuel'), use_container_width=True)
            
            # Vehicle counts per location
            st.subheader('Vehicle Counts per Location')
            location_counts = data['Location'].value_counts().reset_index()
            location_counts.columns = ['Location', 'Count']
            st.bar_chart(location_counts.set_index('Location'), use_container_width=True)
        
        with col2:
            # 10 cheapest cars
            st.subheader('10 Cheapest Cars')
            bottom_10_cheap = data.nsmallest(10, 'Final_Price')
            st.write(bottom_10_cheap)
            
            # Vehicle counts by seats
            st.subheader('Vehicle Counts by Number of Seats')
            seats_counts = data['Seats'].value_counts().reset_index()
            seats_counts.columns = ['Seats', 'Count']
            st.bar_chart(seats_counts.set_index('Seats'), use_container_width=True)
            
            # Vehicle counts by drive
            st.subheader('Vehicle Counts by Drive Type')
            drive_counts = data['Drive'].value_counts().reset_index()
            drive_counts.columns = ['Drive', 'Count']
            st.bar_chart(drive_counts.set_index('Drive'), use_container_width=True)

    # Heatmap
    st.subheader('Correlation Heatmap')
    numeric_data = data.select_dtypes(include='number')  # Select only numeric columns
    fig, ax = plt.subplots(figsize=(18, 12))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    st.pyplot(fig, use_container_width=True)

# Function to display expected sales section
def show_expected_sales():
    st.subheader('Expected Sales')
    
    with st.container():
        col1, col2 = st.columns(2)  # Create two columns for layout
        
        with col1:
            # Sales by Transmission Type (Pie Chart)
            st.subheader('Total Sales by Transmission Type')
            trans_sales = data.groupby('Trans')['Final_Price'].sum().reset_index()
            trans_sales['Final_Price'] = trans_sales['Final_Price'].astype(int)
            
            # Create a pie chart
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.pie(trans_sales['Final_Price'], labels=trans_sales['Trans'], autopct='%1.1f%%', startangle=140)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig, use_container_width=True)
            
            # Sales by Location
            st.subheader('Total Sales by Location')
            location_sales = data.groupby('Location')['Final_Price'].sum().reset_index()
            location_sales['Final_Price'] = location_sales['Final_Price'].astype(int)
            st.bar_chart(location_sales.set_index('Location'), use_container_width=True)
            
            # Sales by Fuel Type
            st.subheader('Total Sales by Fuel Type')
            fuel_sales = data.groupby('Fuel')['Final_Price'].sum().reset_index()
            fuel_sales['Final_Price'] = fuel_sales['Final_Price'].astype(int)
            st.bar_chart(fuel_sales.set_index('Fuel'), use_container_width=True)
        
        with col2:
            # Sales by Steering Type
            st.subheader('Total Sales by Steering Type')
            steering_sales = data.groupby('Steering')['Final_Price'].sum().reset_index()
            steering_sales['Final_Price'] = steering_sales['Final_Price'].astype(int)
            st.bar_chart(steering_sales.set_index('Steering'), use_container_width=True)
            
            # Sales by Color
            st.subheader('Total Sales by Color')
            color_sales = data.groupby('Color')['Final_Price'].sum().reset_index()
            color_sales['Final_Price'] = color_sales['Final_Price'].astype(int)
            st.bar_chart(color_sales.set_index('Color'), use_container_width=True)
            
            # Sales by Drive Type
            st.subheader('Total Sales by Drive Type')
            drive_sales = data.groupby('Drive')['Final_Price'].sum().reset_index()
            drive_sales['Final_Price'] = drive_sales['Final_Price'].astype(int)
            st.bar_chart(drive_sales.set_index('Drive'), use_container_width=True)

# Function to display yearly data section
def show_yearly_data():
    st.subheader('Yearly Data')
    year = st.slider('Select Year', min_value=int(data['Year'].min()), max_value=int(data['Year'].max()), value=int(data['Year'].min()))
    filtered_data = data[data['Year'] == year]
    
    # Display yearly data in a table
    st.dataframe(filtered_data, use_container_width=True)

# Display the selected section
if selected == 'Overview':
    show_overview()
elif selected == 'Expected Sales':
    show_expected_sales()
elif selected == 'Yearly Data':
    show_yearly_data()
