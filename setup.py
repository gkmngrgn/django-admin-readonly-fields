from setuptools import setup

import admin_readonly_fields

description = 'Show readonly fields better in Django admin panel'

with open('README.md') as f:
    long_description = f.read()

setup(
    name='django-admin-readonly-fields',
    version=admin_readonly_fields.__version__,
    description=description,
    author='Gökmen Görgen',
    author_email='gkmngrgn@gmail.com',
    url='https://github.com/gkmngrgn/django-admin-readonly-fields',
    long_description=long_description,
    packages=[
        'admin_readonly_fields',
    ],
    package_data={
        'admin_readonly_fields': [
            'static/admin_readonly_fields/*.js',
            'static/admin_readonly_fields/*.css',
            'static/admin_readonly_fields/img/*',
            'static/django-admin_readonly_fields/*.js',
        ]
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Pygments>=2.2.0'
    ],
    extra_require={
        'markdown': 'Markdown>=2.6.10'
    },
)
