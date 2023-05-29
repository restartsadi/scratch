from flask import Flask, render_template
import pandas as pd
#from flask_restful import Resource, Api, reqparse, abort, marshal, field

#Initialize Flask
app = Flask(__name__)
#api = Api(app)

@app.route('/')
def home():
    xs = {                   
            "tutorial" : "AI & ML",
            "Lecture" : 4,
            "Topic" : "Data Mining",
            "Sponsor" : "Ipsita Computers PTE Limited.",

            "Student" : [{      
                "Name" : "Topu",
                "Phone" : 1303120474,
                "Address" : "H # 07; R # 3; Block # C; Metro Development and Housing Limited"
            }, 
            
            {
                "Name" : "Opu",
                "Phone" : 1803120474,
                "Address" : "H # 07; R # 3; Block # C; Uttara"
            }],
            
        }

    

    return render_template('index.html' , a = xs )


@app.route("/about")
def about():

    return 'The About Page' 

@app.route("/blog")
def blog():

    posts = [ {'name' : 'S. M. Abeer Bin Bashar Sadi', 'subject' : 'Data science', 'program' : 'Hire And Learn', 'organized_by' : 'Ipsita Computers Limited.'}]

    return render_template('blog.html', sunny = False, posts = posts)


@app.route('/blog/<int:blog_id>')
def blog_post(blog_id):

    return "Blog post number : " + str(blog_id)


if __name__ == '__main__':
    app.run()
