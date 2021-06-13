"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, x: list[float]):
        self.values = x

    def __repr__(self) -> str:
        return f"Simpy({self.values}"

    def fill(self, x: float, y: int) -> list[float]: 
        i = 0 
        result: list[float] = []
        while i <= y: 
            result.append(x)
        print(result)
        return result

    
