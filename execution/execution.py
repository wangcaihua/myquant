#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
from abc import ABCMeta, abstractmethod

from stockstar.portfolio import Portfolio

logger = logging.getLogger(__name__)


class ExecutionHandler(object):
    """
    The ExecutionHandler abstract class handles the interaction
    between a set of order objects generated by a Portfolio and
    the ultimate set of Fill objects that actually occur in the
    market. 

    The handlers can be used to subclass simulated brokerages
    or live brokerages, with identical interfaces. This allows
    strategies to be backtested in a very similar manner to the
    live trading engine.
    """

    __metaclass__ = ABCMeta

    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio
        self.events = portfolio.events

    @abstractmethod
    def execute_order(self, event):
        """
        Takes an Order event and executes it, producing
        a Fill event that gets placed onto the Events queue.

        Parameters:
        event - Contains an Event object with order information.
        """
        raise NotImplementedError("Should implement execute_order()")

