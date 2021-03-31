from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse




class Contact(models.Model):

    email           = models.EmailField()
    name            = models.CharField(help_text='Enter a name for your contact...',
                                       max_length=100,
                                       unique=True)
    profile_picture = models.ImageField(upload_to='contacts/images',
                                        blank=True,
                                        null=True)
    
    slug            = models.SlugField(blank=True,
                                       null=True)
    is_selected     = models.BooleanField(default=False)

    def __str__(self):

        return self.name
    
    
    def save(self , *args , **kwargs):

        self.slug = slugify(self.name)
        super(Contact,self).save()
    
    class Meta:

        ordering = ['name']



class Email(models.Model):

    message      = models.TextField()
    receivers    = models.ManyToManyField(Contact,
                                          related_name='emails')
    subject      = models.CharField(max_length=250)

    sender       = models.ForeignKey(User ,
                                     on_delete=models.DO_NOTHING ,
                                     related_name='emails',
                                     null=True)
    date_created = models.DateTimeField(auto_now_add=True,
                                        null=True) 

    def __str__(self):

        return self.subject

    class Meta:

        ordering = ['date_created']

