import random

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect


def index_view(request: WSGIRequest):
    if request.method == "POST":
        name = request.POST.get("name", "no name")
        cat = {
            "name": name,
            "age": 1,
            "satiety": 50,
            "happiness": 50,
            "sleeping": 1,
            "avatar": "/static/jpg/normal.jpeg"
        }
        request.session["cat"] = cat

        return redirect("cat_stats")
    return render(request, "index.html")


def cat_stats(request):
    cat = request.session.get("cat", "no")
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "feed":
            if cat["sleeping"] == 2:
                cat["avatar"] = "/static/jpg/sleeping.jpeg"
            else:
                cat["satiety"] += 15
                cat["happiness"] += 5
                if cat["satiety"] > 100:
                    cat["happiness"] -= 30
                if cat["happiness"] < 20:
                    cat["avatar"] = "/static/jpg/sad.jpeg"
                else:
                    cat["avatar"] = "/static/jpg/happy.jpeg"
        elif action == "play":
            if cat["sleeping"] == 2:
                cat["sleeping"] = 1
                cat["happiness"] -= 5
                if cat["happiness"] < 20:
                    cat["avatar"] = "/static/jpg/sad.jpeg"
                else:
                    cat["avatar"] = "/static/jpg/happy.jpeg"

            else:
                cat["happiness"] += 15
                cat["satiety"] -= 10
                if random.randint(1, 3) == 1:
                    cat["happiness"] = 0
                    cat["avatar"] = "/static/jpg/angry.jpeg"
                elif cat["happiness"] < 20:
                    cat["avatar"] = "/static/jpg/sad.jpeg"
                else:
                    cat["avatar"] = "/static/jpg/happy.jpeg"
        elif action == "sleep":
            cat["sleeping"] = 2
            cat["avatar"] = "/static/jpg/sleeping.jpeg"
    return render(request, "cat_stats.html", context={"cat": cat})
