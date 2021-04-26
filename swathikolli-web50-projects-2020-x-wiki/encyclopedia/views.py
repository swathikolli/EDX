from django.shortcuts import render
from random import randint
from . import util
from django.views.generic import ListView
 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki_entries(request,name):
      s=name
      v=False
      all_names=util.list_entries()
      for m in all_names:
          if (s.casefold() == m.casefold()):
            v=True
            break
        
      if (v==True):
         all_content=util.get_entry(name)
      else:
          all_content="Error 404! oops page not Found"
      return render(request, "encyclopedia/entries.html",{
                  "entry_name":name,
                   "content":all_content
         })
def random(request):
    all_content=util.list_entries()
    n=randint(0,4)
    title=all_content[n];
    content=util.get_entry(title)
    return render(request, "encyclopedia/random.html",{
                  "entry_name":title,
                   "content":content
         })
def search(request):
      if request.method == 'POST':
          name=request.POST['sub']
      s=name
      
      v=False
      all_names=util.list_entries()
      for m in all_names:
          if (s.casefold() == m.casefold()):
            v=True
            break
        
      if (v==True):
         all_content=util.get_entry(name)
         return render(request, "encyclopedia/entries.html",{
                  "entry_name":name,
                   "content":all_content
         })
      else:
        name_list=[]
        for i in all_names:
            j=i.casefold()
            namee=name.casefold()
            if(j.startswith(namee)!= 1):
                continue
            else:
              name_list.append(j)
        return render(request, "encyclopedia/search.html",{
                  "entry_name":name,
                   "name_content":name_list
                  })
def submitted(request):
    m=False
    if request.method == 'POST':
        name=request.POST['title']
        content=request.POST['content']
    all_titles=util.list_entries()
    for i in all_titles:
        if (name.casefold() == i.casefold()):
          m=True;
          break;
        else:
            continue;
    if (m == True):
       return render(request, "encyclopedia/exist.html")
    else:
        util.save_entry(name, content)
        return render(request, "encyclopedia/entries.html", {
            "entry_name":name,
                   "content":content
            })
def editted(request):
    m=False
    if request.method == 'POST':
        name=request.POST['title']
        content=request.POST['content']
    util.save_entry(name, content)
    return render(request, "encyclopedia/entries.html", {
            "entry_name":name,
            "content":content
            })
def cancel(request):
    return render(request, "encyclopedia/newpage.html")
def owner(request):
    return render(request, "encyclopedia/newpage.html")
def edit(request):
    if request.method == 'POST':
        name=request.POST['q'];
    edit_content=util.get_entry(name);
    return render(request, "encyclopedia/edit.html", {
        "name": name,
        "edit_content": edit_content
        })
def delete(request):
    if request.method == 'POST':
        name=request.POST['p'];
    edit_content=util.get_entry(name);
    return render(request, "encyclopedia/delete.html", {
        "name":name})
def newpage(request):
    return render(request, "encyclopedia/newpage.html")
