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
            power_bi_url = "https://app.powerbi.com/view?r=your_report_id"
            components.html(f'<iframe src="{power_bi_url}" width="800" height="600"></iframe>', height=600)
        else:
            st.error("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
