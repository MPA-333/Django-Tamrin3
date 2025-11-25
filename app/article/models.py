from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name="نام",
        blank=False,
        null=False,
    )
    family = models.CharField(
        max_length=32,
        verbose_name="نام خانوادگی",
        blank=False,
        null=False,
    )
    email = models.EmailField(
        verbose_name="ایمیل",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=16,
        verbose_name="شماره تلفن",
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        verbose_name="صفحه شخصی نویسنده",
        blank=True,
        null=True,
    )
    # تحصیلات
    # عنوان شغلی
    isActive = models.BooleanField(
        verbose_name="وضعیت فعال بودن",
        default=True,
    )

    # === #
    def __str__(self):
        return f"{self.name} {self.family} {self.phone}"

    # ===#


class ArticleGroup(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name="اسم گروه",
        blank=False,
        null=False,
    )

    # === #
    def __str__(self):
        return f"{self.title}"

    # ===#


class Article(models.Model):
    aticleGroup = models.ForeignKey(
        ArticleGroup,
        on_delete=models.CASCADE,
        verbose_name="گروه مقاله",
    )
    title = models.CharField(
        max_length=128,
        verbose_name="عنوان مقاله",
        blank=False,
        null=False,
    )
    image = models.ImageField(
        upload_to="image/article/",
        verbose_name="تصویر اصلی",
        blank=False,
        null=False,
    )
    author = models.ManyToManyField(
        Author,
        verbose_name="نویسنده",
    )
    slug = models.SlugField(
        verbose_name="صفحه اصلی مقاله",
        blank=True,
        null=True,
    )
    text = models.CharField(
        max_length=128,
        verbose_name="خلاصه مقاله",
    )
    word = models.CharField(
        max_length=128,
        verbose_name="کلمات کلیدی",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="چکیده مطالب",
    )
    article = models.FileField(
        upload_to="file/article/",
        verbose_name="فایل مقاله (PDF)",
        blank=False,
        null=False,
    )
    registerDate = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاریخ ثبت مقاله",
    )
    publishDate = models.DateTimeField(
        verbose_name="تاریخ انتشار",
        blank=True,
        null=True,
    )
    updateDate = models.DateTimeField(
        verbose_name="تاریخ بروز رسانی",
        blank=True,
        null=True,
    )
    isActive = models.BooleanField(
        verbose_name="وضعیت فعال بودن",
        default=False,
    )
    seen = models.PositiveBigIntegerField(
        verbose_name="تعداد بازدید",
        default=0,
    )

    # === #
    def __str__(self):
        return f"{self.title} {self.text}"

    # ===#


class ArticleGallery(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name="مقاله",
    )
    image = models.CharField(
        max_length=128,
        verbose_name="نام تصاویر",
    )

    # === #
    def __str__(self):
        return f"{self.article} {self.image}"

    # ===#
