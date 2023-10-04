B
    ��e   �               @   s�   d Z ddlmZ ddlmZmZ ddlmZ ddlm	Z	 ddl
mZ edejj�edejd	d
�eded��gZeee	je	jd�7 ZdS )a{  personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
�    )�admin)�path�include)�static)�settings)�viewszadmin/� �home)�namezblog/z	blog.urls)�document_rootN)�__doc__Zdjango.contribr   �django.urlsr   r   Zdjango.conf.urls.staticr   �django.confr   �	portfolior   �site�urlsr	   �urlpatterns�	MEDIA_URL�
MEDIA_ROOT� r   r   �AC:\Users\HP\Desktop\personal_portfolio\personal_portfolio\urls.py�<module>   s   