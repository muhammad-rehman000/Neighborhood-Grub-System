from django.shortcuts import get_object_or_404, render, redirect

from dishes.models import *

def index(request):
    dish_posts = DishPost.objects.all()
    context = {"dish_posts": dish_posts}
    return render(request, "dishes/index.html", context)

def post_detail(request, dish_post_id):
    dish_post = get_object_or_404(DishPost, pk=dish_post_id)
    context = {"dish_post": dish_post}
    if request.user.is_authenticated:
        context["user"] = request.user
    return render(request, "dishes/post_detail.html", context)

def order_dish(request, dish_post_id):
    diner = Diner.objects.get(user=request.user)
    dish_post = DishPost.objects.get(pk=dish_post_id)
    num_servings = request.POST["num_servings"]
    order = Order.objects.create(diner=diner,
                                 dish_post=dish_post,
                                 num_servings=num_servings)
    return redirect("orders")

def orders(request):
    if not request.user.is_authenticated:
        return redirect("dishes")
    else:
        diner = Diner.objects.get(user=request.user)
        orders = Order.objects.filter(diner=diner)
        context = {"orders": orders}
        return render(request, "dishes/orders.html", context)
