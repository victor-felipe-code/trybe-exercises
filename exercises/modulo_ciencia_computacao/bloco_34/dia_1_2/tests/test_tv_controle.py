import pytest
from src.exercicios.tv.exercicio_1 import TV as tv

tv_1 = tv()


"""TESTAR TV"""


def test_ligar_desligar():
    """VERIFICA SE A TV ESTÁ LIGADA"""
    print(tv_1)
    v = tv_1.getter_attribute("ligada")
    assert v


def test_mudar_canal():
    """VERIFICA SE A TV MUDA DE CANAL CORRETAMENTE"""
    canal = tv_1.getter_attribute("canal")
    assert canal == 1
    tv_1.mudar_canal(35)
    canal = tv_1.getter_attribute("canal")
    assert canal == 35

    with pytest.raises(ValueError):
        tv_1.mudar_canal(150)
