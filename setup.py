#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
        name='test_talker_listener',
        version='1.0.0',
        install_requires=[
            'setuptools',
            ],
        data_files=[
            ('share/test_talker_listener', ['package.xml'])
        ],
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'test_node_talker = test_talker_listener.test_node:talker_main',
                'test_node_listener = test_talker_listener.test_node:listener_main'
            ],
        },
        )
