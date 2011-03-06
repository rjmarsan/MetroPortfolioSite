from flask import Flask, render_template, url_for
import navbar
from projects import allprojects
app = Flask(__name__)

RENDER_RAW = False #True



@app.route('/')
@app.route('/<toplevel>')
@app.route('/<toplevel>/')
def show_top_level(toplevel="home"):
    navbaritem = get_navbar_item(toplevel)
    if navbaritem:
        return render_page(navbaritem.text, toplevel=toplevel)
    else:
        return render_page("404404404!", toplevel=toplevel)


def get_navbar_item(toplevel):
    for navbaritem in navbar.items:
        if navbaritem.url == toplevel:
            return navbaritem

def make_navbarlist(toplevel):
    for navbaritem in navbar.items:
        if navbaritem.url.lower() == toplevel.lower():
            navbaritem.selected = True
        else:
            navbaritem.selected = False
    return navbar.items


## The rendering function
def render_page(body, toplevel=None):
    return render_template("template.html", body=body, navigation=make_navbarlist(toplevel))

def render_project(project):
    return render_template("project.html", project=project)

def render_gallery(project_list):
    projects_html = []
    for project in project_list:
        projects_html.append(render_gallery_item(project))
    return render_template("gallery.html", projects=projects_html)

def render_gallery_item(project):
    return render_template("gallery_item.html", project=project)


#get the project object!
def get_project(name):
    for project in allprojects.projects:
        if project.name == name:
            return project 
    return None ## oh no! invalid project!


def get_projects_from_tags(tags):
    goodprojects = []
    for project in allprojects.projects:
        if does_project_contain_tags(project, tags):
            goodprojects.append(project)
    return goodprojects

def does_project_contain_tags(project, tags):
    for tag in tags:
        if not tag in project.tags:
            return False 
    return True













if __name__ == '__main__':
    app.run(debug=True)

