@app.route('/albums/<int:album_id>'
           '/photos/<int:photo_id>/'
           '<string(length=4):action>')
def photo_action(album_id, photo_id, action):
    ...
