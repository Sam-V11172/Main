from django.shortcuts import render
from . models import Post
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

#function based views
# def home(request):
# 	context = {
# 		'posts' : Post.objects.all()
# 	}
# 	return render(request,'blog/home.html',context)

# class based views
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'

class PostDetailView(DetailView):
	model = Post

class PostCreateView(CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})