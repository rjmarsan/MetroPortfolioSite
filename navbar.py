NAVDATA_LOC = "./metrodata/pages/"
from content import Content

class MenuItem:
    title = "title"
    url = "url"
    subitems = []

    data = None

    spacer = False
    
    def __init__(self, title, url=None, subitems=None):
        if not title:
            print "Null item!"
            self.spacer = True
            title = ""
            url = ""
        self.title = title
        if url:
            self.url = url.lower()
        self.subitems = subitems
        self.data = Content(title, url)


gditems = [
    MenuItem('Thing1'),
    MenuItem('Thing2'),
    MenuItem('Thing3'),
    MenuItem('Thing4'),
    MenuItem('Thing5'),
]

photoitems = [
    MenuItem('Portrait', 'Portrait'),
    MenuItem('Stock', 'Stock'),
    MenuItem('Art', 'Art'),
]


items = [ 
    MenuItem('Graphic Design', 'GraphicDesign', gditems),
    MenuItem('Photography', 'Photography', photoitems),
    MenuItem('Sculpture/Drawing', 'SculptureDrawing'),
    MenuItem('Research', 'Research'),
    MenuItem(None, None),
    MenuItem('About', 'About'),
    MenuItem('CV', 'CV'),
    MenuItem('Sample Portfolio', 'SamplePortfolio'),
    MenuItem('Contacts', 'Contacts'),
]
