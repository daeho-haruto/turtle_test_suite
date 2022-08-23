from setuptools import setup

package_name = 'flody_test_suite'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
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
            'pose_sub = flody_test_suite.sub:main',
            'cmd_vel_pub = flody_test_suite.pub:main',
            'test_param = flody_test_suite.param:main',
        ],
    },
)
