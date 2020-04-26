from django.contrib import admin
from post.models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    #which fields want to display
    list_display = ['id','title','slug','author','body','publish','created','updated','status']
    #generate value from other field - prepopulated_fields used.
    prepopulated_fields={'slug':('title',)}
    #filter for admin models
    list_filter=('status','author','created','publish')
    #search according to match
    search_fields=('title','body',)
    #choose data based on id
    #instead of dropdown search box Come
    raw_id_fields = ('author',)
    #for seeing data according date hierarchy
    date_hierarchy = 'publish'
    #top of the column ascending-descending mechanism
    ordering = ['status','publish']

    #ckeditor used
    change_form_template = 'post/admin/change_form.html'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields = ('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
