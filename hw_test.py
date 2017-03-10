# coding: utf-8

import pytest
import hello

def test_01():
    ret = hello.sub('good')
    assert ret != 'Hello! good'
    assert ret == 'Hello! GOOD'

    ret = hello.sub('GOOD')
    assert ret != 'Hello! good'
    assert ret == 'Hello! GOOD'
