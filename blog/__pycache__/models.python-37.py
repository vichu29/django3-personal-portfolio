B
    ��e�   �               @   s"   d dl mZ G dd� dej�ZdS )�    )�modelsc               @   s0   e Zd Zejdd�Ze�� Ze�� Z	dd� Z
dS )�Blog��   )�
max_lengthc             C   s   | j S )N)�title)�self� r   �5C:\Users\HP\Desktop\personal_portfolio\blog\models.py�__str__   s    zBlog.__str__N)�__name__�
__module__�__qualname__r   �	CharFieldr   �	TextField�description�	DateField�dater
   r   r   r   r	   r      s   r   N)�	django.dbr   �Modelr   r   r   r   r	   �<module>   s   