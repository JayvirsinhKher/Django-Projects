from django.shortcuts import render,get_object_or_404
from .models import Post
from taggit.models import Tag

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def post_list_view(request,tag_slug=None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)

    return render(request,'post/post_list.html',{'post_list':post_list,'tag':tag})

#SEO friendly URL

from post.forms import CommentForm

def post_detail_view(request,year,month,day,slug):
    post=get_object_or_404(Post,
                            slug=slug,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    #for comment purpose
    comments = post.comments.filter(active=True)
    csubmit = False
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False) #User only take data like name,email,comment but we require more data related to post
            new_comment.post = post # post object is already there
            new_comment.save()
            csubmit = True
    else:
        form = CommentForm()
    return render(request,'post/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})

# #view all details using id
def post_detail_view1(request,pid):
    post = get_object_or_404(Post,id=pid)
    return render(request,'post/post_detail.html',{'post':post})

from django.views.generic import ListView
class PostListView(ListView):
    model=Post
    paginate_by=1


from django.core.mail import send_mail
from post.forms import EmailSendForm

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent = False
    # form=EmailSendForm()
    if request.method=='POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject ='{}({}) recommends you to read "{}"'.format(cd["name"],cd["email"],post.title)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            thanks = 'Thanks for Sharing\nJayveer Kher\'s Blog'
            msg = 'Read Below Post :\n\n{}\n\n {}\'s Comment :\n{}\n\nURL of post :\t\t{}\n\n{}'.format(post.body,cd['name'],cd['comment'],post_url,thanks)
            mail = cd['email']
            to = cd['to']
            # read data and send mail
            send_mail(subject,msg,mail,[to])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'post/sharebyemail.html',{'form':form,'post':post,'sent':sent})
