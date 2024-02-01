from django.contrib import admin
from django.db import models
from quiz.models import UserProfile,AllQuestion
from django.forms import Textarea

class YourModelAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'question':
            # Replace 'your_text_field_name' with the actual name of your text field.
            kwargs['widget'] = admin.widgets.AdminTextareaWidget(attrs={'rows': 5, 'cols': 40})
            # You can adjust the 'rows' and 'cols' values to fit your desired size.

        return super().formfield_for_dbfield(db_field, **kwargs)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(AllQuestion,YourModelAdmin)