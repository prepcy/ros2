from setuptools import setup

package_name = 'pkg03_example_server_py'

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
            'node_cli = pkg03_example_server_py.node_cli:main',
            'node_ser = pkg03_example_server_py.node_ser:main',
        ],
    },
)
