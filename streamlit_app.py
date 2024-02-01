import streamlit as st

def main():
    st.title("Drink Tracking App")

    # Drink button
    if st.button("Drink!"):
        st.write("You drank something!")

    # Data page button
    if st.button("Data"):
        st.write("Navigate to the data page.")

    # Sidebar with user information form
    st.sidebar.title("User Information")
    name = st.sidebar.text_input("Name:")
    weight = st.sidebar.number_input("Weight (kg):", min_value=0)
    gender = st.sidebar.radio("Gender:", ("Male", "Female"))

    if st.sidebar.button("Save"):
        # Process user information (not implemented yet)
        st.sidebar.write(f"Name: {name}, Weight: {weight} kg, Gender: {gender}")

if __name__ == "__main__":
    main()
