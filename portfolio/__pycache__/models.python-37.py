B
    ��e8  �               @   s"   d dl mZ G dd� dej�ZdS )�    )�modelsc               @   sD   e Zd Zejdd�Zejdd�Zejdd�Zej	dd�Z
dd	� Zd
S )�Project�d   )�
max_length��   zportfolio/images/)�	upload_toT)�blankc             C   s   | j S )N)�title)�self� r   �:C:\Users\HP\Desktop\personal_portfolio\portfolio\models.py�__str__	   s    zProject.__str__N)�__name__�
__module__�__qualname__r   �	CharFieldr	   �description�
ImageField�image�URLField�urlr   r   r   r   r   r      s
   r   N)�	django.dbr   �Modelr   r   r   r   r   �<module>   s   