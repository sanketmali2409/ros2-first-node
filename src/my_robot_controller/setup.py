from setuptools import setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/all_nodes_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sanket',
    maintainer_email='you@example.com',
    description='My Robot Controller package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = my_robot_controller.publisher_node:main',
            'subscriber_node = my_robot_controller.subscriber_node:main',
            'service_node = my_robot_controller.service_node:main',
            'client_node = my_robot_controller.client_node:main',
            'led_service = my_robot_controller.led_service:main',
            'led_client = my_robot_controller.led_client:main',
            'yes_no_service = my_robot_controller.yes_no_service:main',
            'yes_no_client = my_robot_controller.yes_no_client:main',
        ],
    },
)
