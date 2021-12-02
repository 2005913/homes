from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
    #한 번에 보여주는 Choicetext의 숫자 결정

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text']}),
                 ('Date information',{'fields':['pub_date'],'classes':['collapse']}),] #필드 순서 변경
    inlines = [ChoiceInLine] #Choice모델 클래스 같이 보기
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)



