from __future__ import annotations
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact(_Jac.Walker):

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'Hello, world!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact_with_body(_Jac.Walker):
    name: str

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'Hello, ' + self.name + '!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('add_numbers', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class simple_calculator(_Jac.Walker):
    num1: float
    num2: float

    def add_numbers(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'The sum is ' + str(self.num1 + self.num2) + '.'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('check_number', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class number_checker(_Jac.Walker):
    number: int

    def check_number(self, _jac_here_: _Jac.RootType) -> None:
        if self.number >= 100:
            _Jac.report({'response': 'Number greater than or equal to 100.'})
        else:
            _Jac.report({'response': 'Number less than 100.'})