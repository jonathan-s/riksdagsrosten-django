from django.contrib import admin

from .models import UserProfile
from .models import UserVote
from .models import UserSimilarity

class UserProfileAdmin(admin.ModelAdmin):
    pass

class UserVoteAdmin(admin.ModelAdmin):
    pass

class UserSimilarityAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserVote, UserVoteAdmin)
admin.site.register(UserSimilarity, UserSimilarityAdmin)
