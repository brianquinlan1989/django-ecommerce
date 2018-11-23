from django.shortcuts import render, redirect
from .forms import ReviewForm


# Create your views here.

def make_review(request, id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.author = request.user
        review.product_id = id
        review.save()

        return redirect('product_detail', id = id, )
    else:
        form = ReviewForm()
        return render(request, "reviews/review_form.html", {'form':form})
    

