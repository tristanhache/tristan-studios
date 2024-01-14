from flask import Flask, render_template

app = Flask(__name__)

movie_data = {
    'movie1': {
        'title': 'Cure for Cancer',
        'id': '1',
        'description': 'Matéo Belmont is a brilliant but reclusive scientist known for his groundbreaking research. When he discovers a potential cure for cancer, he is faced with moral dilemmas, corporate greed, and the complexities of scientific ethics. Gabriela Mendoza, a journalist with a passion for truth, becomes entangled in the story, uncovering a web of secrets that could change the world.',
        'release_date': 'January 1, 2028',
        'genre': 'Action',
        'image': 'static/img/moviePlaceholder.png',
        'video_url': 'lokiS1.mp4',  # Replace with the actual video URL
    },
    'movie2': {
        'title': 'Movie 2',
        'id': '2',
        'description': 'Description of Movie 2.',
        'release_date': 'February 1, 2023',
        'genre': 'Adventure',
        'image': 'static/img/moviePlaceholder.png',
        'video_url': 'lokiS1.mp4',  # Replace with the actual video URL
    }
}

serie_data = {
    'show1': {
        'title': 'Inventor Mateo',
        'id': '1',
        'description': 'In a future world where technology has reached unparalleled heights, Mateo Harrington is a visionary inventor who embarks on a quest to pioneer the exploration of the multiverse. His invention, a multiversal watch, enabled him to send a daring explorer into alternate realities, leading to a journey of discovery, danger, and profound revelations.',
        'episodes':'9',
        'release_date': 'March 15, 2030',
        'genre': 'Action',
        'image': 'static/img/moviePlaceholder.png',
        'video_url': 'lokiS1.mp4',  # Replace with the actual video URL
        'next_episode_url': 'lokiS2.mp4',  # Replace with the actual next episode URL
    },
    'show2': {
        'title': 'Show 2',
        'id': '2',
        'description': 'Description of Show 2.',
        'episodes':'9',
        'release_date': 'April 1, 2023',
        'genre': 'Comedy',
        'image': 'static/img/moviePlaceholder.png',
        'video_url': 'lokiS1.mp4',  # Replace with the actual video URL
        'next_episode_url': 'lokiS2.mp4',  # Replace with the actual next episode URL
    },
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    # Logic to fetch movie details (replace with your database logic)
    movie = {'title': f'Movie {movie_id}', 'id': movie_id}
    return render_template('movie_detail.html', movie=movie)

@app.route('/series/<int:series_id>')
def series_detail(series_id):
    # Logic to fetch series details (replace with your database logic)
    series = {'title': f'Series {series_id}', 'id': series_id}
    return render_template('series_detail.html', series=series)

if __name__ == '__main__':
    app.run(debug=True)
