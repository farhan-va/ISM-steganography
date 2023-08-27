# Importing the necessary modules
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image
from stegano import lsbset
from stegano.lsbset import generators

# Creating the basic Python Image Steganography functions
def main_encryption(img, text, new_image_name):
    # This function will take the arguments, create a new image, encode it and save it to the same directory
    image = Image.open(img, 'r')
    if (len(text) == 0) or (len(img) == 0) or (len(new_image_name) == 0):
        mb.showerror(
            "Error", 'You have not put a value! Please put all values before pressing the button')
    new_image = image.copy()
    new_image = lsbset.hide(img, text, generators.eratosthenes())
    new_image_name += '.png'
    new_image.save(new_image_name, 'png')


def main_decryption(img):
    # This function will decode the image given to it and extract the hidden message from it
    image = Image.open(img, 'r')
    data = lsbset.reveal(image, generators.eratosthenes())
    print(data)
    text_entry.delete(0, END)
    text_entry.insert(END, data)

# Creating the button functions
def encode_image():
    encode_wn = Toplevel(root)
    encode_wn.title("Encode an Image")
    encode_wn.geometry('600x220')
    encode_wn.resizable(0, 0)
    encode_wn.config(bg='AntiqueWhite')
    Label(encode_wn, text='Encode an Image', font=(
        "Roboto", 15), bg='AntiqueWhite').place(x=220, rely=0)
    Label(encode_wn, text='Enter the path to the image(with extension):', font=("Times New Roman", 13),
          bg='AntiqueWhite').place(x=10, y=50)
    Label(encode_wn, text='Enter the data to be encoded:', font=("Times New Roman", 13), bg='AntiqueWhite').place(
        x=10, y=90)
    Label(encode_wn, text='Enter the output file name (without extension):', font=("Times New Roman", 13),
          bg='AntiqueWhite').place(x=10, y=130)
    img_path = Entry(encode_wn, width=35)
    img_path.place(x=350, y=50)
    text_to_be_encoded = Entry(encode_wn, width=35)
    text_to_be_encoded.place(x=350, y=90)
    after_save_path = Entry(encode_wn, width=35)
    after_save_path.place(x=350, y=130)
    Button(encode_wn, text='Encode the Image', font=('Helvetica', 12), bg='PaleTurquoise', command=lambda:
           main_encryption(img_path.get(), text_to_be_encoded.get(), after_save_path.get())).place(x=220, y=175)


def decode_image():
    decode_wn = Toplevel(root)
    decode_wn.title("Decode an Image")
    decode_wn.geometry('600x300')
    decode_wn.resizable(0, 0)
    decode_wn.config(bg='Bisque')
    Label(decode_wn, text='Decode an Image', font=(
        "Roboto", 15), bg='Bisque').place(x=220, rely=0)
    Label(decode_wn, text='Enter the path to the image (with extension):', font=("Times New Roman", 12),
          bg='Bisque').place(x=10, y=50)
    img_entry = Entry(decode_wn, width=35)
    img_entry.place(x=350, y=50)
    Button(decode_wn, text='Decode the Image', font=('Helvetica', 12), bg='PaleTurquoise', command=lambda:
           main_decryption(img_entry.get())).place(x=220, y=90)
    Label(decode_wn, text='Text that has been encoded in the image:', font=("Times New Roman", 12), bg='Bisque').place(
        x=180, y=130)
    global text_entry
    text_entry = Entry(decode_wn, width=94)
    text_entry.place(x=15, y=160, height=100)


# Initializing the window
root = Tk()
root.title('Image Steganography')
root.geometry('300x200')
root.resizable(0, 0)
root.config(bg='NavajoWhite')
Label(root, text='Image Steganography', font=('Roboto', 15), bg='NavajoWhite',
      wraplength=300).place(x=50, y=20)
Button(root, text='Encode', width=25, font=('Times New Roman', 13), bg='SteelBlue', command=encode_image).place(
    x=30, y=80)
Button(root, text='Decode', width=25, font=('Times New Roman', 13), bg='SteelBlue', command=decode_image).place(
    x=30, y=130)
# Finalizing the window
root.update()
root.mainloop()
