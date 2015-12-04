from setuptools import setup, find_packages
 
setup(
    name='deploy_utils',
    packages=find_packages(),
    install_requires=[
        'boto>=2.38',
        'fabric>=1.10.1',
        'django-fab-deploy>=0.7.5'
    ],
    entry_points={
        'console_scripts': [
            'launch_amazon_linux=deploy_utils.test_script:amazon_linux_test_battery',
            'launch_centos6=deploy_utils.test_script:centos6_test_battery',
            'temp=deploy_utils.test_script:temp'
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose']
)
