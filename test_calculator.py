
import pytest
import sys
sys.path.append('..')
from pythoncode.Calculator import Calculator
import yaml
import math

def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'],datas['add']['ids'],datas['div']['datas'],datas['div']['ids'])



class TestCalc:
    datas:list = get_datas()
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    #相加功能
    @pytest.mark.parametrize("a,b, result",datas[0],ids=datas[1])
    def test_add(self,a,b,result):
        assert result == self.calc.add(a,b)

    # "a,b,result", datas[2]
    #相除功能
    @pytest.mark.parametrize("a,b, result",datas[2],ids=datas[3])
    def test_div(self,a,b,result):
        if b != 0:
            assert result == self.calc.div(a,b)
        elif b == 0:
            with pytest.raises(ZeroDivisionError):
                self.calc.div(a,b)


