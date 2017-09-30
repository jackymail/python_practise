from django.contrib import admin

# Register your models here.

from.models import Question,Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fields = [
        (None,{'fields' : ['question_text']}),
        ('Date Infomation',{'fields' : ['pub_date'],
         'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')


admin.site.register(Question,QuestionAdmin)

admin.site.register(Choice)
