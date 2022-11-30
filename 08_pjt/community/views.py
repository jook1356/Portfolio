from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import JsonResponse
from .models import Review, Comment
from .forms import ReviewForm, CommentForm


@require_GET
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.filter(parent_comment=None)
    comments_count = Comment.objects.filter(review=review_pk).count()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
        'comments_count': comments_count,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments_count = Comment.objects.filter(review=review_pk).count()
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()

            context = {
                "request_user": request.user.username,
                "comment_content": comment.content,
                "comment_user": comment.user.username,
                "comment_pk": comment.pk,
                "comments_count": comments_count,
                "review_pk": review_pk,
            }
            return JsonResponse(context)
    else:
        return redirect('accounts:login')
    # return render(request, 'community/detail.html', context)


@require_POST
def create_cocomment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments_count = Comment.objects.filter(review=review_pk).count()
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.review = review
        new_comment.parent_comment = comment
        new_comment.user = request.user
        new_comment.save()
        context = {
            "request_user": request.user.username,
            "cocomment_content": new_comment.content,
            "cocomment_user": new_comment.user.username,
            "cocomment_pk": new_comment.pk,
            "comments_count": comments_count,
            "review_pk": review_pk,
        }
        return JsonResponse(context)
    # context = {
    #     'comment_form': comment_form,
    #     'review': review,
    #     'comments': review.comment_set.all(),
    # }
    return redirect('community:detail', review.pk)



@require_POST
def update_comment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment_form = CommentForm(request.POST, instance=comment)
    if comment_form.is_valid():
        new_comment = comment_form.save()
        new_comment.save()
        context = {
            "request_user": request.user.username,
            "comment_content": new_comment.content,
            "comment_user": new_comment.user.username,
            "comment_pk": new_comment.pk,
        }
        return JsonResponse(context)
    # context = {
    #     'comment_form': comment_form,
    #     'review': review,
    #     'comments': review.comment_set.all(),
    # }
    return redirect('community:detail', review.pk)





@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            is_liked = False 
        else:
            review.like_users.add(user)
            is_liked = True
        context = {
            "is_liked": is_liked,
            "like_users_count": review.like_users.count()
        }
        return JsonResponse(context)
    return redirect('accounts:login')


@require_POST
def comment_like(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        user = request.user

        if comment.like_users.filter(pk=user.pk).exists():
            comment.like_users.remove(user)
            is_liked = False 
        else:
            comment.like_users.add(user)
            is_liked = True
        context = {
            "is_liked": is_liked,
            "like_users_count": comment.like_users.count()
        }
        return JsonResponse(context)
    return redirect('accounts:login')



@require_POST
def delete_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user == comment.user:
        comment.delete()
        context = {
            'delete': comment_pk,
        }
        return JsonResponse(context)

