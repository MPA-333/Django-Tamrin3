from django.db import models
from django.utils import timezone


class VisitorGroup(models.Model):
    TITLES = [(1, "عمومی"),(2, "گروهی یا دانشجویی"),(3, "خارجی")]
    code = models.PositiveSmallIntegerField(verbose_name="عنوان", choices=TITLES)

    def __str__(self):
        return f"{self.TITLES[self.code-1][1]}"

    class Meta:
        verbose_name = "گروه بازدید کننده"
        verbose_name_plural = "گروه بازدید کنندگان"


class Place(models.Model):
    code = models.PositiveIntegerField(verbose_name="کد", blank=False, null=False, unique=True, default=1)
    title = models.CharField(verbose_name="عنوان", max_length=150, blank=False, null=False)
    image = models.CharField(verbose_name="عکس", max_length=150, blank=True, default="garden1.jpg")
    time = models.TimeField(verbose_name="زمان بازدید", blank=False, null=False)
    date = models.DateField(verbose_name="روز بازدید", blank=False, null=False)
    rule = models.CharField(verbose_name="قوانین و مررات", max_length=350, blank=False, null=False)
    detail = models.TextField(verbose_name="اطلاعات بیشتر", blank=True)
    registerDateTime = models.DateTimeField(verbose_name="زمان ثبت مکان", blank=False, null=False, default=timezone.now)

    def __str__(self):
        return f"{self.code}-{self.title}"

    class Meta:
        verbose_name = "مکان"
        verbose_name_plural = "مکان ها"


class TicketPrice(models.Model):
    code = models.PositiveIntegerField(verbose_name="کد بهای بلیط", blank=False, null=False, unique=True, default=1)
    group = models.ForeignKey(VisitorGroup, on_delete=models.CASCADE, verbose_name="گروه")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="مکان")
    price = models.CharField(verbose_name="قیمت", max_length=9, blank=False, null=False, default=500000)

    def __str__(self):
        return f"{self.group}-{self.place}: {self.price} تومان"

    class Meta:
        verbose_name = "بهای بلیط"
        verbose_name_plural = "بهای بلیط ها"


class Message(models.Model):
    code = models.PositiveIntegerField(verbose_name="کد", blank=False, null=False, unique=True, default=1)
    name = models.CharField(verbose_name="نام", max_length=120, blank=False, null=False)
    family = models.CharField(verbose_name="نام خانوادگی", blank=True)
    email = models.EmailField(verbose_name="ایمیل", unique=True)
    subject = models.CharField(verbose_name="موضوع پیام", max_length=350, blank=False, null=False)
    text = models.TextField(verbose_name="متن پیام", blank=False, null=False)
    registerDate = models.DateTimeField(verbose_name="تاریخ ثبت پیام", blank=False, null=False, default=timezone.now)
    STATUS = [(True, "فعال"),(False, "غیرفعال")]
    isActive = models.BooleanField(verbose_name="وضعیت پیام", choices=STATUS, blank=False, null=False)

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"
