from flask import Flask, render_template
import requests
from post import Post

posts  = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
print(posts)
post_objects = []

for post in posts:
    post_object = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_object)
    

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    return render_template("post.html", post=post_objects[index-1])    


if __name__ == "__main__":
    app.run(debug=True)