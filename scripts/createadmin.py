#!/usr/bin/env python

from django.contrib.auth.models import User
if User.objects.count() == 0:
    admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    admin.save()