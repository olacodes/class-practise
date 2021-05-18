# from django.shortcuts import render

# Create your views here.

from forum.models.forum import Forum
from django.views.generic.list import ListView

class ForumListView(ListView):
  model = Forum
  context_object_name = "forums"
  template_name = 'forum_list.htm'