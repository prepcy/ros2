from setuptools import setup

package_name = 'pkg06_example_action_py'

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
    maintainer='root',
    maintainer_email='yuanjilin@cdjrlc.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_action = pkg06_example_action_py.node_action:main',
            'node_action_cli = pkg06_example_action_py.node_action_cli:main',
        ],
    },
)
