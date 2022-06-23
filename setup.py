#!/usr/bin/env python3

'''
Python distutils setup file for gym-copter module.

Copyright (C) 2022 Yosef Tamene, Simon D. Levy

MIT License
'''

from setuptools import setup

setup(
    name='dynamixel_ax12',
    version='0.1',
    install_requires=['gym', 'numpy', 'Box2D', 'opencv-python'],
    description='Python library for Dynamixel AX-12 servo',
    packages=['ax12'],
    author='Yosef Tamene, Simon D. Levy',
    author_email='simon.d.levy@gmail.com',
    url='https://github.com/simondlevy/dynamixel-ax12',
    license='MIT',
    platforms='Linux'
    )
