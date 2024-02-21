import tkinter as tk
from PIL import Image, ImageTk
import cv2

def show_frame():
    ret, frame = cap.read()
    if ret:
        # Convert frame to RGB for tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk  # Keep a reference to avoid garbage collection
        label.configure(image=imgtk)

        label.after(10, show_frame)
    else:
        print("Error: Unable to capture frame from camera.")

# Create the tkinter window
window = tk.Tk()
window.geometry("800x600")
window.title("Window with Webcam")

# Create the webcam frame
webcam_frame = tk.Frame(window, width=640, height=480)
webcam_frame.pack(side=tk.LEFT)

# Create the webcam label
label = tk.Label(webcam_frame)
label.pack()

# Initialize and open the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to open webcam.")
    exit(1)

# Start showing the webcam feed
show_frame()

# Start the tkinter mainloop
window.mainloop()

# Release the webcam resource
cap.release()
cv2.destroyAllWindows()
