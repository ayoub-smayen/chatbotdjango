from django.contrib import admin

# Register your models here.
from .models import User, Question, Subject,Quiz, TakenQuiz,Student,Answer,UserProfile
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(TakenQuiz)
admin.site.register(Student)
admin.site.register(Answer)
admin.site.register(UserProfile)