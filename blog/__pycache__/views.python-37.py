B
    ��e_  �               @   s0   d dl mZmZ ddlmZ dd� Zdd� ZdS )	�    )�render�get_object_or_404�   )�Blogc             C   s   t j�� }t| dd|i�S )Nzblog/all_blogs.html�blogs)r   �objects�allr   )�requestr   � r
   �4C:\Users\HP\Desktop\personal_portfolio\blog\views.py�	all_blogs   s    
r   c             C   s   t t|d�}t| dd|i�S )N)�pkzblog/detail.html�blog)r   r   r   )r	   Zblog_idr   r
   r
   r   �detail   s    r   N)�django.shortcutsr   r   �modelsr   r   r   r
   r
   r
   r   �<module>   s   