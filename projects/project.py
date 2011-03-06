"""
For my love!

see awesomeproject.py for stuff and junk!

E><3!
"""

class Project:
    name = 'AwesomeProject'  #this is the 'shortcode' name, so it needs to be safe for URLs
    tags = ['amazing', 'sexy']  #a list of all of the tags of your work.  be descriptive!
    title = 'The Awesome Project <3' #the actual title of your beautiful work.  this does not need to be URL safe


    ### BIG TIP!!!! All images, static pages, css, everything, must go in /static/, or else Python thinks the URL is supposed to be handled by my program.
    #gallery stuff
    gallery_thumb = 'gallery_thumb.jpg' #the url of the gallery thumbnail image.
    gallery_custom_css = 'display:none;' #in case you want to manipulate the thumbnail a bit

    #infoview stuff
    infoview_thumb = 'infoview_thumb.jpg' #the url of the infoview image, presumably bigger than the gallery image
    infoview_description = "/path/to/info.html" #the url of the desription. i'm making this a link because it's a pain to do html here.

    #project view stuff
    details_images = [
        {'url':'/path/to/detail1.jpg', 'description' : 'something about the image!'},
        {'url':'/path/to/detail2.jpg', 'description' : 'something about the image... 2!'},
                    ] # a list of images that will be included on the details page
    details_description = 'static/projects/AwesomeProject/details_awesome.html'  #the url of the details page. it's pretty broad-ranging. once again, only put images and stuff in static/!


    #this stuff is automatic, no toque <3
    details_description_string = ""
    infoview_description_string = ""



    def __init__(self):
        try:
            details = open("./"+self.details_description, 'r')
            self.details_description_string = details.read()
            self.infoview_description_string = open("./"+self.infoview_description, 'r').read()
        except:
            print "Error loading stuff! in : "+self.name

if __name__ == "__main__":
    p = Project()

