from tkinter import filedialog, Tk, Label, Button
import pandas as pd
import numpy as np 
import openai
OPENAI_API_KEY="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"
# Initialize filepath as a global variable
filepath = ""
# ORG_ID = "org-zzIbtX6OqmaPSF9vvgqVTW51"
# API_KEY= "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"

def select_file():
    def browseFiles():
        global filepath  # Declare filepath as global
        filepath = filedialog.askopenfilename(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        if filepath:
            label_file_explorer.configure(text="File Opened:\n" + filepath)
            window.destroy()  # Close the Tkinter window after selecting the file

    # Create the root window
    window = Tk()

    # Set window title
    window.title('File Explorer')

    # Set window size
    window.geometry("300x150")

    # Set window background color
    window.config(background="black")

    # Create a File Explorer label
    label_file_explorer = Label(window,
                                text="File Explorer",
                                width=20,
                                fg="blue")

    button_explore = Button(window,
                            text="Browse",
                            width=10,
                            command=browseFiles)

    button_exit = Button(window,
                        text="Exit",
                        width=10,
                        command=window.destroy)  # Exit button destroys the window

    # Grid method is chosen for placing
    # the widgets at respective positions
    label_file_explorer.grid(column=1, row=1, padx=10, pady=10)
    button_explore.grid(column=1, row=2, padx=10, pady=10)
    button_exit.grid(column=1, row=3, padx=10, pady=10)

    # Let the window wait for any events
    window.mainloop()

    # Now you can access 'filepath' globally after the Tkinter window is closed
    print("Selected File:", filepath)
    return filepath




def get_file_type (filepath):
    return filepath.split(".")[-1]

#accomodtae other file types
# use username
def get_file_details(filepath):
    ext = get_file_type(filepath)
    if ext!="json":
        df = pd.read_csv(filepath)
        shape = df.shape
        column_names = df.columns
        print(f"Hi Jenny \nYou have opened {ext} file type.\nShape :{shape} \ncolumn names : {column_names}")
        return df
    



def summary(df):
    gpt_client = openai.Client(api_key=OPENAI_API_KEY)
    response = gpt_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"summarise the dataset {df.head(5)} ",
            }
        ],
       #model="gpt-3.5-turbo",
        model="gpt-4o",
    )
    print("\n")
    print (response.choices[0].message.content)






file_path = select_file()
dataframe = get_file_details(filepath=file_path)
summary(dataframe)





    

