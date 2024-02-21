# flames_app.py
import streamlit as st

def calculate_flames(name1, name2):
    # Remove common characters
    name1_set = set(name1.lower())
    name2_set = set(name2.lower())
    common_chars = name1_set.intersection(name2_set)

    # Calculate remaining characters
    remaining_chars = len(name1) + len(name2) - 2 * len(common_chars)

    # FLAMES categories
    categories = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]
    result_index = (remaining_chars % len(categories)) - 1

    return categories[result_index]

def main():
    st.title("FLAMES Game")
    st.write("Enter two names to determine your relationship:")

    name1 = st.text_input("Name 1")
    name2 = st.text_input("Name 2")

    if st.button("Calculate"):
        if name1 and name2:
            result = calculate_flames(name1, name2)
            st.success(f"Your relationship category: *{result}*")
        else:
            st.warning("Please enter both names.")

if _name_ == "_main_":
    main()
