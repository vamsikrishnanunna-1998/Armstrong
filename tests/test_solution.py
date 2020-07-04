import os,sys
sys.path.append(os.getcwd())
from solution import checkArmstrong
import pytest


@pytest.mark.parametrize('x,result',[
    (153,True),(1000,False),(370,True),(371,True),(420,False),(407,True)
])
def test_checkArmstrong(x,result):
    assert checkArmstrong(x) == result