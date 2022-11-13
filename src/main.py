import tkinter as tk
from imdb_api import *
from api import API
global comment_index

def clear_frames():
    for widget in top_frame.winfo_children():
        widget.destroy()
    for widget in center_frame.winfo_children():
        widget.destroy()
    for widget in bottom_frame.winfo_children():
        widget.destroy()

def first_display():
    clear_frames()
    tk.Label(top_frame, text="Film name :").pack()
    prompt = tk.Entry(center_frame)
    prompt.pack()
    button = tk.Button(bottom_frame,text='Get films', command=lambda : display_corresponding_movies(prompt))
    button.pack()
    root.mainloop()

def display_corresponding_movies(prompt):

    film_asked=prompt.get()
    clear_frames()
    corresponding_films=ImdbRequest.search_corresponding_movies(film_asked)
    label_title = tk.Label(top_frame, text='Corresponding films')
    label_title.pack()
    lb = tk.Listbox(center_frame)
    lb.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)
    a=0
    for i in corresponding_films:
        lb.insert(a, i['title'])
        a=a+1
    tk.Button(bottom_frame, text='Show Selected', command=lambda : display_reviews(lb,corresponding_films)).pack()

def get_selected_movie_from_listbox(listbox):
    for item in listbox.curselection():
        film_index=item + 1
    return film_index


def display_reviews(listbox,corresponding_films):
    global comment_index
    comment_index = 0
    film_index=get_selected_movie_from_listbox(listbox)
    clear_frames()
    reviews = ImdbRequest.request_review(corresponding_films[film_index]['id'])
    var_title= tk.StringVar()
    label_title = tk.Label(top_frame, textvariable=var_title)
    var_title.set('review number {} out of {}'.format(1, len(reviews)))
    tk.Button(bottom_frame, text='back to menu', command=lambda: first_display()).pack()
    tk.Button(bottom_frame, text='next comment', command=lambda: change_comment(reviews,var,comment,label_title,var_title)).pack()
    label_title.pack()
    var = tk.StringVar()
    comment = tk.Message(center_frame, textvariable=var)
    if (reviews == []):
        var.set("No comment found for this selection")
    else:
        var.set(reviews[comment_index])
    comment.pack()

    def change_comment(reviews , var_com, comment,label_title,var_title):
        global comment_index
        if (comment_index < len(reviews)):

            comment_index = comment_index + 1
            var_com.set(reviews[comment_index])
            var_title.set('review number {} out of {}'.format(comment_index+1, len(reviews)))
            comment.pack()
            label_title.pack()




if __name__ == '__main__':
    root = tk.Tk()
    top_frame=tk.Frame(root, width=400, height=50)
    center_frame=tk.Frame(root, width=400, height=300)
    bottom_frame=tk.Frame(root, width=400, height=100)
    top_frame.pack()
    center_frame.pack()
    bottom_frame.pack()
    first_display()
