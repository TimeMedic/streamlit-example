import streamlit as st

# Function to render page content based on selection
def render_page(page):
    if page == "Main":
        show_main_page()
    elif page == "Data":
        show_data_page()

# Function to display the main page content
def show_main_page():
    # Button to navigate to the data page (on the right side)
    col1, col2 = st.columns([9, 1])
    with col2:
        if st.button("Data"):
            st.session_state.page = "Data"
        
    # Drink button
    col1, col2, col3 = st.columns([2, 1,2])
    with col2:
        if st.button("Drink!"):
            st.write("You drank something!")

# Function to display the data page content
def show_data_page():

    # Button to go back to the main page (top right corner)
    col1, col2 = st.columns([9, 1])
    with col2:
        if st.button("Back"):
            st.session_state.page = "Main"
        
    st.write('data...')

def save_user_info(name, weight, sex):
    # Here you can implement the logic to save user information
    # For now, let's just print it
    st.write("User information saved:")
    st.write(f"Name: {name}")
    st.write(f"Weight: {weight} kg")
    st.write(f"Sex: {sex}")


# Main function to handle navigation and rendering
def main():
    # Initialize page state
    if "page" not in st.session_state:
        st.session_state.page = "Main"

    st.title("Drink Tracker App")
    
    # Render page content
    render_page(st.session_state.page)
    
    with st.sidebar:
        st.subheader("User Information")
        name = st.text_input("Name")
        weight = st.number_input("Weight (kg)")
        sex = st.selectbox("Sex", ["Male", "Female"])

        if st.button("Save"):
            save_user_info(name, weight, sex)

if __name__ == "__main__":
    main()
