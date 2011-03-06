CONTENT_LOC = "./metrodata/pages/"


class Content:
    title = "title"
    url = "url"

    text = ""
    
    def __init__(self, title, url=None, subitems=None):
        self.title = title
        if url:
            self.url = url.lower()
        try:
            self.text = open(CONTENT_LOC+url, 'r').read()
        except:
            print "Error loading navbar  in : "+self.title



items = [ 
    Content('Graphic Design', 'GraphicDesign'),
    Content('Photography', 'Photography'),
    Content('Sculpture/Drawing', 'SculptureDrawing'),
    Content('Research', 'Research'),
    Content('About', 'About'),
    Content('CV', 'CV'),
    Content('Sample Portfolio', 'SamplePortfolio'),
    Content('Contacts', 'Contacts'),

    Content('Home', 'Home'),
]
