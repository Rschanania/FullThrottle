from django.contrib import admin
from posts.models import Posts ,Category,Gallery
from django.contrib.auth.models import User,Group
from user.models import ActivityPeriod


#use for change admin details 
class MyAdminSite(admin.AdminSite):
    site_header="Kaamkr.com"
    site_title="Kaamkr"
    index_title="Kaamkr Adminstraion's"

class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('__str__',)
    list_display_links = ()
    list_filter = ()
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    
    preserve_filters = True
    inlines = []

    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    popup_response_template = None

    # Actions
    actions = [] 
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    

#we use this as a global and out side the class then
def change_to_Withdrown(ModelAdmin,request,queryset):
    queryset.update(status="w")

change_to_Withdrown.short_description="chane status to withdrawn"

class PostsAdmin(admin.ModelAdmin):
    def change_status(self,request,queryset):#if we usse inside the class as local 
        queryset.update(status="d")
    change_status.short_description="Change Status to Draft"
    list_display = ('title',"show_content","user",'show_thumbnail','status')
    list_display_links = ()
    list_filter = ()
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ("status",)
    search_fields = ()
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    
    preserve_filters = True
    inlines = []

    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    popup_response_template = None

    # Actions
    actions = ['change_status',change_to_Withdrown]
   
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True



class GalleryAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    list_display_links = ()
    list_filter = ()
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    
    preserve_filters = True
    inlines = []

    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    popup_response_template = None

    # Actions
    actions = []
   
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True


# admin.site.register(Posts,PostsAdmin) This is working with the default site setting
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Gallery,GalleryAdmin)

admin_site=MyAdminSite()#for the custom admin site 
admin_site.register(Posts,PostsAdmin)
admin_site.register(Category,CategoryAdmin)
admin_site.register(Gallery,GalleryAdmin)
admin_site.register(User)#we have to register all models manuly 
admin_site.register(Group)
admin_site.register(ActivityPeriod)