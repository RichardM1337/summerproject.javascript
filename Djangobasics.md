**Don't forget to CD app and activate scripts!!**

```
mainapp/
    manage.py
    mainapp/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

        > __init__.py = tells mainapp/ that this is a python package
        > settings.py = settings for project
        > asgi.py and wsgi.py = compatibility for certain ASGI and > > WSGI web servers
        > urls.py = url dedications. aka table of contents
```
```
secondapp/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    urls.py
```
### -models (database layout)

### -admin (to register models)


### -views (send information to website)


# urls 
urlpatterns=[
    path("wherever/youwanttheurl/", views.callsfunctionofsiteneeded, anythingnecessary=todefine)
    
    >for referencing other URL confs #
    
mainapp/urls.py
path("subapp/", include(subapp.urls))
]

## Url Paths
1. Route = URL pattern (no GET/POST or domain). EG: myapp and myapp/?page=3 both come from the route "myapp"
2. view = for httprequests
3. (optional) kwargs = for keyword arguments
4. (optional) name = to name your URL throughout different templates


# how to load templates
- define template = loader.get_tmeplate("secondapp/template.html")
- return HttpResponse(template.render(stuff,morestuff))
OR
- return render(blah blah, "secondapp/template.html", blah blah)
### generic views
there are types of views that make work easier by classifying what kind of view you're using. all you need is to define the model at that point and add .asview() in the urls.
you can change the model's name by using context_object_name

# 404 Errors
```
from django.http import Http404
try: 
    yourcode
except variable.DoesNotExist:
    raise Http404("Does not exist)
return render(everything else, context)
```
OR
```
from django.shortcuts import get_object_or_404, render

varialbe = get_object_or_404(whateveryouwantthevariabletobe)
```
Aforementioned code can also work with lists with get_list_or_404
# Terminal Commands
py manage.py collectstatic -- collects static files (after setting STATIC_ROOT)
django-admin startproject {projectname}  -- makes project
python manage.py startapp {subname}  -- creates {subname} app
python manage.py runserver -- starts server
python manage.py migrate -- looks at settings.installed_apps foranything necessary to do such as creating tables for databases
python manage.py makemigrations {subapp} -- update models as migration
python manage.py sqlmigrate {subapp} {migrationnumberbasedonmigrationsfolder} -- takes migration names and returns their SQL
python manage.py check -- checks if there are any issues before any migrations are made
python manage.py shell -- tests api
python manage.py test {subapp} -- runs tests.py $###.

# Tips
- put another secondapp subdirectory sothat django is able to differentiate between said templates folder and another similarly named templates folder.
- bypass saved Django cache (like css) with CTRL + F5