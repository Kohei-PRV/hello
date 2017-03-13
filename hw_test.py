# coding: utf-8

import pytest
import hello

def test_01():
    ret = hello.sub('good')
    assert ret != 'Hello! good'

def test_02():
    ret = hello.sub('GOOD')
    assert ret == 'Hello! GOOD'
