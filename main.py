# import tkinter as tk
# from gui import NewsApp

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = NewsApp(root)
#     root.mainloop()



import tkinter as tk
from gui import NewsApp

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x700")
    app = NewsApp(root)
    root.mainloop()