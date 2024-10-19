import os
import streamlit as st

# Function to list files from the folder and generate download links
def list_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    files = [f for f in files if f.endswith('.pdf')]  # Filter to show only PDFs
    return files

# Main function to build the Streamlit app
def main():
    st.title("Books Repository")
    
    # List the categories of books
    categories = {
        "Python": "data/python",
        "Machine Learning (ML)": "data/ml",
        "Deep Learning (DL)": "data/dl",
        "Artificial Intelligence (AI)": "data/ai",
        "Java": "data/java"
    }
    
    # Dropdown for selecting the category
    category = st.sidebar.selectbox("Select a Category", list(categories.keys()))

    st.subheader(f"Books in {category}")
    
    # Get the folder path based on category selection
    folder_path = categories[category]
    
    # List files in the selected category
    files = list_files_in_folder(folder_path)

    if files:
        for file in files:
            file_path = os.path.join(folder_path, file)
            
            # Show file name and provide download link
            with open(file_path, "rb") as f:
                file_bytes = f.read()
                st.write(f"📘 {file}")
                st.download_button(label="Download", data=file_bytes, file_name=file, mime="application/pdf")
    else:
        st.write("No books available in this category.")

if __name__ == "__main__":
    main()
