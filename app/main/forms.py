from django import forms
from django.core.exceptions import ValidationError


def nameValid(value):
    return True

def familyValid(value):
    return True

def emailValid(value):
    return True

def subjectValid(value):
    return True

def textValid(value):
    return True


class MessageForm(forms.Form):
    name = forms.CharField(label="نام", max_length=120, required=True)
    family = forms.CharField(label="نام خانوادگی", max_length=120, required=False)
    email = forms.EmailField(label="ایمیل", required=True)
    subject = forms.CharField(label="موضوع", max_length=120, required=True)
    text = forms.CharField(widget=forms.Textarea(), label="متن پیام", required=True)

    def clean_name(self):
        name = self.cleaned_data["name"]
        if nameValid==False:
            raise ValidationError("نام صحیح نیست.")
        return name
    
    def clean_family(self):
        family = self.cleaned_data["family"]
        if familyValid==False:
            raise ValidationError("نام خانوادگی صحیح نیست.")
        return family
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if emailValid==False:
            raise ValidationError("ایمیل صحیح نیست.")
        return email
    
    def clean_subject(self):
        subject = self.cleaned_data["subject"]
        if subjectValid==False:
            raise ValidationError("موضوع صحیح نیست.")
        return subject
    
    def clean_text(self):
        text = self.cleaned_data["text"]
        if textValid==False:
            raise ValidationError("متن صحیح نیست.")
        return text
    


            




    # code = models.PositiveIntegerField(verbose_name="کد", blank=False, null=False, default=1)
    # name = models.CharField(verbose_name="نام", max_length=120, blank=False, null=False)
    # family = models.CharField(verbose_name="نام خانوادگی", blank=True)
    # email = models.EmailField(verbose_name="ایمیل", unique=True)
    # subject = models.CharField(verbose_name="موضوع پیام", max_length=350, blank=False, null=False)
    # text = models.TextField(verbose_name="متن پیام", blank=False, null=False)
    # registerDate = models.DateTimeField(verbose_name="تاریخ ثبت پیام", blank=False, null=False, default=timezone.now)
    # STATUS = [(True, "فعال"),(False, "غیرفعال")]
    # isActive = models.BooleanField(verbose_name="وضعیت پیام", choices=STATUS, blank=False, null=False)