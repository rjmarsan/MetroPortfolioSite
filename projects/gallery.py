"""
For my love!

When you make a new project, copy this file. rename it to whatever you want.
Please leave the 'class Project:' in tact, other than that, do whatever you want!

then just change the parameters here to fit your project, and save it in the same folder!


As an annoyance, that I sincerely apologize for, there's a file in this folder called allprojects.py, this project must be added to it.
Look inside that file for a description of how to add it!


then enjoy the love!

E><3!
"""
import os
import project

class Project(project.Project):
    project_dir = '/static//' 

    name = 'Fo'  #this is the 'shortcode' name, so it needs to be safe for URLs
    tags = ['P']  #a list of all of the tags of your work.  be descriptive!
    title = 'F' #the actual title of your beautiful work.  this does not need to be URL safe


    ### BIG TIP!!!! All images, static pages, css, everything, must go in /static/, or else Python thinks the URL is supposed to be handled by my program.
    #gallery stuff
    gallery_thumb = project_dir+'gallery_thumb.jpg' #the url of the gallery thumbnail image.
    gallery_custom_css = '' #in case you want to manipulate the thumbnail a bit

    #infoview stuff
    infoview_thumb = project_dir+'infoview_thumb.jpg' #the url of the infoview image, presumably bigger than the gallery image
    infoview_description = project_dir+"info.html" #the url of the desription. i'm making this a link because it's a pain to do html here.

    #project view stuff
    gallery = True 

    gallery_data = []

    def __init__(self):
        print "loading stuff for: "+self.project_dir
        project.Project.__init__(self)
        self.gallery_data = []
        self.gallery = True
        if not self.gallery_data:
            try:
                #Let's go looking for it!
                for file in os.listdir("./"+self.project_dir+"full/"):
                    self.gallery_data.append( { self.gallery_thumburl: self.project_dir+"thumb/"+file, 
                                                self.gallery_full   : self.project_dir+"full/"+file,
                                                self.gallery_text   : ""})
            except:
                print "EEK! error loading gallery: "+self.name
        print self.gallery_data


if __name__ == "__main__":
    x = Project()
