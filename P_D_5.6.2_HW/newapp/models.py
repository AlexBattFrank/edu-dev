from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import Sum

from allauth.account.forms import SignupForm
from django.utils.datetime_safe import datetime


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0  # creating intermediate variable
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0  # creating intermediate variable
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return f'{self.authorUser}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"Category: {self.name}"


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    REGULATION = 'REG'
    POLLS = 'POL'
    SATELLITE = 'SAT'

    CATEGORY_CHOICES = (
        (NEWS, 'News'),
        (ARTICLE, 'Articles'),
        (REGULATION, 'Regulation'),
        (POLLS, 'POL'),
        (SATELLITE, 'SAT'),
    )
    categoryType = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default=ARTICLE)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    body = models.TextField()
    rating = models.SmallIntegerField(default=0)

    # " Добавим абсолютный путь чтобы после создания нас перебрасывало на главную страницу "

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})  # возможен переход по id статьи\новости

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.body[0:60] + '...'

    def __str__(self):
        return f'{self.dateCreation}, {self.title}, {self.body}, {self.author}'


class PostCategory(models.Model):
    postThought = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThought = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Категория: {self.categoryThought}, Пост: {self.postThought}'


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    # def __str__(self):
    #     return self.commentPost.author.authorUser.username + '___' + str(self.id)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.text}, {self.dateCreation}, {self.rating}'


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
