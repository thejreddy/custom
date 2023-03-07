from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.ForeignKey(User,related_name="Profile",on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.TextField(max_length=30, blank=True)
    subscribed = models.BooleanField(default=False)
    subscribed1 = models.BooleanField(default=False)
    subscribed2= models.BooleanField(default=False)
    subscribed3 = models.BooleanField(default=False)
    subscribed4= models.BooleanField(default=False)
    subscribed5 = models.BooleanField(default=False)
    subscribed6 = models.BooleanField(default=False)
    subscribed7 = models.BooleanField(default=False)
    subscribed8 = models.BooleanField(default=False)
    subscribed9 = models.BooleanField(default=False)
    subscribed10 = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)




class brainjaiib(models.Model):
    user= models.ForeignKey(User,related_name="UserB",on_delete=models.CASCADE, null=True)
    subscribed = models.OneToOneField(Profile,related_name="ProfileB",on_delete=models.CASCADE, null=True)
    a1011 = models.FloatField(null=True)
    a1012 = models.FloatField(null=True)
    a1013 = models.FloatField(null=True)
    a1021 = models.FloatField(null=True)
    a1022 = models.FloatField(null=True)
    a1023 = models.FloatField(null=True)
    a1031 = models.FloatField(null=True)
    a1032 = models.FloatField(null=True)
    a1033 = models.FloatField(null=True)
    a1041 = models.FloatField(null=True)
    a1042 = models.FloatField(null=True)
    a1043 = models.FloatField(null=True)
    a1051 = models.FloatField(null=True)
    a1052 = models.FloatField(null=True)
    a1053 = models.FloatField(null=True)
    a1061 = models.FloatField(null=True)
    a1062 = models.FloatField(null=True)
    a1063 = models.FloatField(null=True)
    a1071 = models.FloatField(null=True)
    a1072 = models.FloatField(null=True)
    a1073 = models.FloatField(null=True)
    a1081 = models.FloatField(null=True)
    a1082 = models.FloatField(null=True)
    a1083 = models.FloatField(null=True)
    a1091 = models.FloatField(null=True)
    a1092 = models.FloatField(null=True)
    a1093 = models.FloatField(null=True)
    a1101 = models.FloatField(null=True)
    a1102 = models.FloatField(null=True)
    a1103 = models.FloatField(null=True)
    a1111 = models.FloatField(null=True)
    a1112 = models.FloatField(null=True)
    a1113 = models.FloatField(null=True)
    a1121 = models.FloatField(null=True)
    a1122 = models.FloatField(null=True)
    a1123 = models.FloatField(null=True)
    a1131 = models.FloatField(null=True)
    a1132 = models.FloatField(null=True)
    a1133 = models.FloatField(null=True)
    a1141 = models.FloatField(null=True)
    a1142 = models.FloatField(null=True)
    a1143 = models.FloatField(null=True)
    a1151 = models.FloatField(null=True)
    a1152 = models.FloatField(null=True)
    a1153 = models.FloatField(null=True)
    Diplaylist = ['profile', 'overallrunningaverage']

    def __str__(self):
        return str(self.subscribed)

    @property
    def username(self):
        username = self.profile.user
        def __str__(self):
            return username

    @property
    def runavg(self):
        easytotal= self.sub_code_score_101_1+ self.sub_code_score_102_1+self.sub_code_score_103_1+self.sub_code_score_104_1+self.sub_code_score_105_1+self.sub_code_score_106_1+self.sub_code_score_107_1+self.sub_code_score_108_1+self.sub_code_score_109_1+self.sub_code_score_110_1+self.sub_code_score_111_1+self.sub_code_score_112_1+self.sub_code_score_113_1+self.sub_code_score_114_1+self.sub_code_score_115_1
        mediumtotal = self.sub_code_score_101_2+ self.sub_code_score_102_2+self.sub_code_score_103_2+self.sub_code_score_104_2+self.sub_code_score_105_2+self.sub_code_score_106_2+self.sub_code_score_107_2+self.sub_code_score_108_2+self.sub_code_score_109_2+self.sub_code_score_110_2+self.sub_code_score_111_2+self.sub_code_score_112_2+self.sub_code_score_113_2+self.sub_code_score_114_2+self.sub_code_score_115_2
        difficulttotal = self.sub_code_score_101_1+ self.sub_code_score_102_1+self.sub_code_score_103_1+self.sub_code_score_104_1+self.sub_code_score_105_1+self.sub_code_score_106_1+self.sub_code_score_107_1+self.sub_code_score_108_1+self.sub_code_score_109_1+self.sub_code_score_110_1+self.sub_code_score_111_1+self.sub_code_score_112_1+self.sub_code_score_113_1+self.sub_code_score_114_1+self.sub_code_score_115_1
        easycoefficient = easytotal/15
        mediumcoefficient = mediumtotal/15
        difficultcoefficient = difficulttotal/15
        overallrunningaverage = easycoefficient*0.45+mediumcoefficient*0.35+difficultcoefficient*20
        return overallrunningaverage




@receiver(post_save, sender=Profile)
def create_user_brain(sender, instance, created, **kwargs):
    if instance.subscribed==True:
        if not created:
            brainjaiib.objects.get_or_create(subscribed=instance)






class braincaiib(models.Model):
    user = models.ForeignKey(User,related_name="User1",on_delete=models.CASCADE, null=True)
    subscribed1 = models.OneToOneField(Profile,related_name="Profile1",on_delete=models.CASCADE, null=True)
    sub_code_score_101_1 = models.FloatField(null=True)
    sub_code_score_101_2 = models.FloatField(null=True)
    sub_code_score_101_3 = models.FloatField(null=True)
    sub_code_score_102_1 = models.FloatField(null=True)
    sub_code_score_102_2 = models.FloatField(null=True)
    sub_code_score_102_3 = models.FloatField(null=True)
    sub_code_score_103_1 = models.FloatField(null=True)
    sub_code_score_103_2 = models.FloatField(null=True)
    sub_code_score_103_3 = models.FloatField(null=True)
    sub_code_score_104_1 = models.FloatField(null=True)
    sub_code_score_104_2 = models.FloatField(null=True)
    sub_code_score_104_3 = models.FloatField(null=True)
    sub_code_score_105_1 = models.FloatField(null=True)
    sub_code_score_105_2 = models.FloatField(null=True)
    sub_code_score_105_3 = models.FloatField(null=True)
    sub_code_score_106_1 = models.FloatField(null=True)
    sub_code_score_106_2 = models.FloatField(null=True)
    sub_code_score_106_3 = models.FloatField(null=True)
    sub_code_score_107_1 = models.FloatField(null=True)
    sub_code_score_107_2 = models.FloatField(null=True)
    sub_code_score_107_3 = models.FloatField(null=True)
    sub_code_score_108_1 = models.FloatField(null=True)
    sub_code_score_108_2 = models.FloatField(null=True)
    sub_code_score_108_3 = models.FloatField(null=True)
    sub_code_score_109_1 = models.FloatField(null=True)
    sub_code_score_109_2 = models.FloatField(null=True)
    sub_code_score_109_3 = models.FloatField(null=True)
    sub_code_score_110_1 = models.FloatField(null=True)
    sub_code_score_110_2 = models.FloatField(null=True)
    sub_code_score_110_3 = models.FloatField(null=True)
    sub_code_score_111_1 = models.FloatField(null=True)
    sub_code_score_111_2 = models.FloatField(null=True)
    sub_code_score_111_3 = models.FloatField(null=True)
    sub_code_score_112_1 = models.FloatField(null=True)
    sub_code_score_112_2 = models.FloatField(null=True)
    sub_code_score_112_3 = models.FloatField(null=True)
    sub_code_score_113_1 = models.FloatField(null=True)
    sub_code_score_113_2 = models.FloatField(null=True)
    sub_code_score_113_3 = models.FloatField(null=True)
    sub_code_score_114_1 = models.FloatField(null=True)
    sub_code_score_114_2 = models.FloatField(null=True)
    sub_code_score_114_3 = models.FloatField(null=True)
    sub_code_score_115_1 = models.FloatField(null=True)
    sub_code_score_115_2 = models.FloatField(null=True)
    sub_code_score_115_3 = models.FloatField(null=True)
    Diplaylist = ['profile', 'overallrunningaverage']



    @property
    def username(self):
        username = self.profile.user
        def __str__(self):
            return username

    @property
    def runavg(self):
        easytotal= self.sub_code_score_101_1+ self.sub_code_score_102_1+self.sub_code_score_103_1+self.sub_code_score_104_1+self.sub_code_score_105_1+self.sub_code_score_106_1+self.sub_code_score_107_1+self.sub_code_score_108_1+self.sub_code_score_109_1+self.sub_code_score_110_1+self.sub_code_score_111_1+self.sub_code_score_112_1+self.sub_code_score_113_1+self.sub_code_score_114_1+self.sub_code_score_115_1
        mediumtotal = self.sub_code_score_101_2+ self.sub_code_score_102_2+self.sub_code_score_103_2+self.sub_code_score_104_2+self.sub_code_score_105_2+self.sub_code_score_106_2+self.sub_code_score_107_2+self.sub_code_score_108_2+self.sub_code_score_109_2+self.sub_code_score_110_2+self.sub_code_score_111_2+self.sub_code_score_112_2+self.sub_code_score_113_2+self.sub_code_score_114_2+self.sub_code_score_115_2
        difficulttotal = self.sub_code_score_101_1+ self.sub_code_score_102_1+self.sub_code_score_103_1+self.sub_code_score_104_1+self.sub_code_score_105_1+self.sub_code_score_106_1+self.sub_code_score_107_1+self.sub_code_score_108_1+self.sub_code_score_109_1+self.sub_code_score_110_1+self.sub_code_score_111_1+self.sub_code_score_112_1+self.sub_code_score_113_1+self.sub_code_score_114_1+self.sub_code_score_115_1
        easycoefficient = easytotal/15
        mediumcoefficient = mediumtotal/15
        difficultcoefficient = difficulttotal/15
        overallrunningaverage = easycoefficient*0.45+mediumcoefficient*0.35+difficultcoefficient*20
        return overallrunningaverage
