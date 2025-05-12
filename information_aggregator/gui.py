# # --- gui.py ---
# import tkinter as tk
# from tkinter import ttk, scrolledtext
# from aggregator import Aggregator
# from visualizer import visualize_sources, visualize_wordcloud

# class NewsApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("📰 News Aggregator")
#         self.root.configure(bg="#f5f7fa")

#         # Category Selection
#         self.category = tk.StringVar(value="technology")
#         categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

#         sidebar = tk.Frame(root, bg="#e3eaf2", padx=10, pady=10)
#         sidebar.pack(side=tk.LEFT, fill=tk.Y)

#         tk.Label(sidebar, text="Select Category:", font=("Arial", 12), bg="#e3eaf2").pack(pady=(0, 5))
#         dropdown = ttk.Combobox(sidebar, values=categories, textvariable=self.category, state='readonly')
#         dropdown.pack(pady=(0, 15))

#         fetch_btn = tk.Button(sidebar, text="🔍 Fetch News", font=("Arial", 11), bg="#0d47a1", fg="white", command=self.show_news)
#         fetch_btn.pack(pady=5, fill='x')

#         viz1_btn = tk.Button(sidebar, text="📊 Show Source Chart", font=("Arial", 11), bg="#1976d2", fg="white", command=self.show_visualization_sources)
#         viz1_btn.pack(pady=5, fill='x')

#         viz2_btn = tk.Button(sidebar, text="☁️ Show Word Cloud", font=("Arial", 11), bg="#388e3c", fg="white", command=self.show_wordcloud)
#         viz2_btn.pack(pady=5, fill='x')

#         # Display Area
#         self.display_frame = tk.Frame(root, bg="#f5f7fa")
#         self.display_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         self.canvas = tk.Canvas(self.display_frame, bg="#f5f7fa", highlightthickness=0)
#         self.scrollbar = tk.Scrollbar(self.display_frame, orient=tk.VERTICAL, command=self.canvas.yview)
#         self.scrollable_frame = tk.Frame(self.canvas, bg="#f5f7fa")

#         self.scrollable_frame.bind(
#             "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#         )

#         self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)

#         self.canvas.pack(side="left", fill="both", expand=True)
#         self.scrollbar.pack(side="right", fill="y")

#     def show_news(self):
#         for widget in self.scrollable_frame.winfo_children():
#             widget.destroy()

#         aggregator = Aggregator(category=self.category.get())
#         articles = aggregator.get_combined_data()
#         self.articles = articles

#         for i, article in enumerate(articles, 1):
#             card = tk.Frame(self.scrollable_frame, bg="white", bd=1, relief="solid", padx=10, pady=10)
#             card.pack(pady=8, padx=10, fill="x", expand=True)

#             title = tk.Label(card, text=f"{i}. {article['title']}", font=("Arial", 14, "bold"), fg="#0d47a1", bg="white", wraplength=800, justify="left")
#             title.pack(anchor="w")

#             source = tk.Label(card, text=f"Source: {article['source']['name']}", font=("Arial", 10, "italic"), fg="#555", bg="white")
#             source.pack(anchor="w", pady=(5, 0))

#             content = tk.Label(card, text=article['full_content'], font=("Arial", 11), fg="#333", bg="white", wraplength=800, justify="left")
#             content.pack(anchor="w", pady=(5, 0))

#     def show_visualization_sources(self):
#         if hasattr(self, 'articles') and self.articles:
#             visualize_sources(self.articles)

#     def show_wordcloud(self):
#         if hasattr(self, 'articles') and self.articles:
#             visualize_wordcloud(self.articles)







# --- Enhanced Modern gui.py ---
import tkinter as tk
from tkinter import ttk
from aggregator import Aggregator
from visualizer import visualize_sources, visualize_wordcloud

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📰 News Aggregator")
        self.root.configure(bg="#F9FAFB")
        self.root.geometry("1280x720")

        self.category = tk.StringVar(value="technology")
        categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

        # Apply style for ttk widgets
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6, font=("Segoe UI", 11), relief="flat", background="#4F46E5", foreground="white")
        style.configure("TCombobox", padding=5, font=("Segoe UI", 11))

        # Sidebar frame
        sidebar = tk.Frame(self.root, bg="#EEF2FF", width=240)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(sidebar, text="🔍 Select Category", font=("Segoe UI", 12, "bold"), bg="#EEF2FF", fg="#1E40AF").pack(pady=(20, 5), anchor="w", padx=15)
        category_dropdown = ttk.Combobox(sidebar, values=categories, textvariable=self.category, state="readonly")
        category_dropdown.pack(padx=15, fill=tk.X)

        ttk.Button(sidebar, text="Fetch News", command=self.show_news).pack(pady=(20, 10), padx=15, fill=tk.X)
        ttk.Button(sidebar, text="📊 Source Chart", command=self.show_visualization_sources).pack(pady=5, padx=15, fill=tk.X)
        ttk.Button(sidebar, text="☁ Word Cloud", command=self.show_wordcloud).pack(pady=5, padx=15, fill=tk.X)

        # Title bar
        title_bar = tk.Frame(self.root, bg="#F9FAFB")
        title_bar.pack(fill=tk.X, pady=(10, 5))
        tk.Label(title_bar, text="📰 News Dashboard", font=("Segoe UI", 22, "bold"), bg="#F9FAFB", fg="#111827").pack(padx=20, anchor="w")

        # Main display area with scrollable canvas
        self.canvas_frame = tk.Frame(self.root, bg="#F9FAFB")
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="#F9FAFB", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#F9FAFB")

        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def show_news(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        aggregator = Aggregator(category=self.category.get())
        articles = aggregator.get_combined_data()
        self.articles = articles

        for i, article in enumerate(articles, 1):
            card = tk.Frame(self.scrollable_frame, bg="white", bd=1, relief="groove")
            card.pack(pady=10, padx=20, fill="x")

            title = tk.Label(card, text=f"{i}. {article['title']}", font=("Segoe UI", 13, "bold"), fg="#1D4ED8", bg="white", wraplength=1000, justify="left")
            title.pack(anchor="w", padx=10, pady=(10, 5))

            source = tk.Label(card, text=f"Source: {article['source']['name']}", font=("Segoe UI", 10, "italic"), fg="#6B7280", bg="white")
            source.pack(anchor="w", padx=10)

            content = tk.Label(card, text=article['full_content'], font=("Segoe UI", 11), fg="#111827", bg="white", wraplength=1000, justify="left")
            content.pack(anchor="w", padx=10, pady=(5, 10))

    def show_visualization_sources(self):
        if hasattr(self, 'articles') and self.articles:
            visualize_sources(self.articles)

    def show_wordcloud(self):
        if hasattr(self, 'articles') and self.articles:
            visualize_wordcloud(self.articles)
