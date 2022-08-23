from setuptools import setup
import os
from glob import glob


package_name = 'turtle_test_suite'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (os.path.join('share', package_name, 'launch'), 
            glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'config'), 
            glob(os.path.join('config', '*.yaml'))),
        # (os.path.join('share', package_name, 'action'), 
        #     glob(os.path.join('action', '*.action'))),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='daeho',
    maintainer_email='daeho@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sub = ' + package_name + '.sub:main',
            'pub = ' + package_name + '.pub:main',
            'turtle_test_suite_node = ' 
                + package_name + '.turtle_test_suite_node:main',
        ],
    },
)
