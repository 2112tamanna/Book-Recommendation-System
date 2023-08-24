from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pickle.load(open('model/popular.pkl', 'rb'))
pt = pickle.load(open('model/pt.pkl', 'rb'))
books = pickle.load(open('model/books.pkl', 'rb'))
similarity_scores = pickle.load(open('model/similarity_scores.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0]

    if len(index) == 0:
        # No book found with the given name
        error_message = "No book found similar to the name you have entered or the name of the book is wrong."
        return render_template('recommend.html', error_message=error_message)

    index = index[0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        items = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]

        image_url = list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)
        if image_url:
            items.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            items.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            items.extend(image_url)
        
            data.append(items)

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
