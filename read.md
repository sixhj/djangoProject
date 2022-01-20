

# cmd

```

python manage.py startapp  [name]   # 创建应用
python manage.py makemigrations     # 生成变动文件
python manage.py migrate            # 修改数据库

python manage.py createsuperuser    # 创建用户

admin admin



```


# supervisord 


使用多线程启动


文件位置


/etc/supervisor/supervisord.conf


circusd  
使用 supervisord  ->  uwsgi   ->  python
 


# 启动 supervisor


supervisor



启动circusd  启动 gunicorn


        location /appointment_admin/protocol/ {
                add_header Cache-Control "no-cache";
                alias /usr/docker_project/bus_apply_server/bus_apply_server_running/protocol/;
        }



# 创建应用


=====
Polls
=====

Polls is a Django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.