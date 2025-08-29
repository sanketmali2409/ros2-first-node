from setuptools import setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sanket',
    maintainer_email='sanket@example.com',
    description='My robot controller nodes',
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
            'my_first_node = my_robot_controller.my_first_node:main',
        ],
    },
)
