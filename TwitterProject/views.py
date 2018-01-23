from django.shortcuts import render
from django.http import HttpResponse
from .models import Account,Post,Tag


def index(request):
    return render(request, 'TwitterProject/index.html')
# Create your views here.
def userInfo(request,account_id):
    account = Account.objects.filter(pk=account_id)
    return render(request, 'TwitterProject/UserInfo.html', {'account': account})

def get_accounts(request):
    collection_account = Account.objects.all()    
    return render(request, 'TwitterProject/UserCollection.html', {'collection_account': collection_account})

def get_posts(request,account_id):

    collection_posts = Post.objects.filter(Owner__pk=account_id)
    return render(request, 'TwitterProject/PostCollection.html', {'collection_posts': collection_posts})

def get_tags(request):
    collection_tags = Tag.objects.all()
    return render(request, 'TwitterProject/TagCollection.html', {'collection_tags': collection_tags})

def get_post_tag(request,tag_id):
    collection_posts = Post.objects.filter(TagCollection__pk=tag_id)
    return render(request, 'TwitterProject/PostCollection.html', {'collection_posts': collection_posts})

