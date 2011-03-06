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
            self.url = url
        else:
            self.url = title
        self.subitems = subitems
        if subitems:
            for sub in subitems:
                sub.url = str(url)+"/"+sub.url
        self.data = Content(title, url)


gditems = [
    MenuItem('Good Roots', 'GoodRoots'),
]

photoitems = [
    MenuItem('Portrait', 'Portrait'),
    MenuItem('Food', 'Food'),
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
