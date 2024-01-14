from flask import Flask, render_template

app = Flask(__name__)

# Sample media data (replace with your actual data)
media_data = {
    'movie1': {
        'title': 'Movie 1',
        'description': 'Description of Movie 1.',
        'release_date': 'January 1, 2023',
        'genre': 'Action',
        'image': 'movie1.jpg',
        'video_url': 'https://example.com/movie1.mp4',  # Replace with the actual video URL
    },
    'movie2': {
        'title': 'Movie 2',
        'description': 'Description of Movie 2.',
        'release_date': 'February 1, 2023',
        'genre': 'Adventure',
        'image': 'movie2.jpg',
        'video_url': 'https://example.com/movie2.mp4',  # Replace with the actual video URL
    },
    'show1': {
        'title': 'Show 1',
        'description': 'Description of Show 1.',
        'release_date': 'March 1, 2023',
        'genre': 'Drama',
        'image': 'show1.jpg',
        'video_url': 'https://example.com/show1.mp4',  # Replace with the actual video URL
        'next_episode_url': 'https://example.com/show2.mp4',  # Replace with the actual next episode URL
    },
    'show2': {
        'title': 'Show 2',
        'description': 'Description of Show 2.',
        'release_date': 'April 1, 2023',
        'genre': 'Comedy',
        'image': 'show2.jpg',
        'video_url': 'https://example.com/show2.mp4',  # Replace with the actual video URL
        'next_episode_url': 'https://example.com/show3.mp4',  # Replace with the actual next episode URL
    },
    # Add more media items as needed
}

@app.route('/')
def index():
    return render_template('index.html', media_data=media_data)

@app.route('/media/<media_id>')
def media(media_id):
    if media_id in media_data:
        return render_template('media_info.html', media=media_data[media_id])
    else:
        return 'Media not found', 404

@app.route('/video_player/<media_id>')
def video_player(media_id):
    if media_id in media_data:
        return render_template('video_player.html', media=media_data[media_id])
    else:
        return 'Media not found', 404

if __name__ == '__main__':
    app.run(debug=True)
