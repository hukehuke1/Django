#coding:utf-8


import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

if django.VERSION >= (1, 7):#自动判断django版本
    django.setup()


def main():
    from blog.models import Blog
    f = open('oldblog.txt')
    for line in f:
        title, content = line.split('****')
        Blog.objects.create(title=title, content=content)
    f.close()


if __name__ == "__main__":
    main()
    print("Done!")
