Don't forget to CD app and activate scripts!!

mainapp/
    manage.py
    mainapp/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

        __init__.py = tells mainapp/ that this is a python package
        settings.py = settings for project
        asgi.py and wsgi.py = compatibility for certain ASGI and WSGI web servers
        urls.py = url dedications. aka table of contents


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


urls 
urlpatterns=[
    path("wherever/youwanttheurl/", views.callsfunctionofsiteneeded, anythingnecessary=todefine)
    
    >for referencing other URL confs #
    
mainapp/urls.py
path("subapp/", include(subapp.urls))
]


views (for whats on the screen)




python manage.py runserver