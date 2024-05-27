import streamlit as st
import streamlit.components.v1 as components

# Function to verify the password
def verify_password(password):
    # Define the correct password
    correct_password = "uDgywm:4jVqdiDf"
    return password == correct_password

# Streamlit app
def main():
    st.title("Power BI Dashboard Viewer")
    
    # Ask for the password
    password = st.text_input("Enter the password to view the dashboard:", type="password")
    
    if password:
        # Check if the password is correct
        if verify_password(password):
            st.success("Password correct! Loading the dashboard...")
            
            # Embed the Power BI dashboard
            power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZDVmYTdmYjctOWYxMy00YjRlLTk4OTUtOTQyYzc5YzA5ZWI5IiwidCI6ImI0YTc0NjQyLWFkOTMtNGQ1Ni1iOWVjLWU2YzRmZTA4MGE3ZSIsImMiOjN9"
            components.html(f'<iframe src="{power_bi_url}" width="600" height="375"></iframe>', height=400)
        else:
            st.error("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
