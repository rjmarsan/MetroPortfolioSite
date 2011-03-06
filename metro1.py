from flask import Flask, render_template
import navbar
from projects import allprojects
app = Flask(__name__)

RENDER_RAW = False #True

@app.route('/')
def hello_world():
    return render_page("Hello world!")

@app.route('/gallery/<tag>')
def show_gallery(tag):
    projects = get_projects_from_tags([tag])
    if projects:
        if RENDER_RAW:
            return render_gallery(projects)
        else:
            return render_page(render_gallery(projects))
    else:
        return "liar!"

@app.route('/show/gallery/<projectname>')
def show_gallery_view(projectname):
    project = get_project(projectname)
    if project:
        return render_gallery_item(project)
    else:
        return "liar!"



@app.route('/info/<tag>')
def show_info(tag):
    return "Fancy infoness: "+tag

@app.route('/show/<projectname>')
def show_project(projectname):
    project = get_project(projectname)
    if project:
        if RENDER_RAW:
            return render_project(project)
        else:
            return render_page(render_project(project))
    else:
        return "liar!"





## The rendering function
def render_page(body):
    return render_template("template.html", body=body, navigation=navbar.items)

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

