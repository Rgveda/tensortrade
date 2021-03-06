# Copyright 2019 The TensorTrade Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod

from tensortrade.trades import Trade


class SlippageModel(object, metaclass=ABCMeta):
    """A model for simulating slippage on an exchange trade."""

    def __init__(self):
        pass

    @abstractmethod
    def fill_order(self, trade: Trade) -> Trade:
        """Simulate slippage on a trade ordered on a specific exchange.

        Arguments:
            trade: The trade executed on the exchange.

        Returns:
            A filled `Trade` with the `price` and `amount` adjusted for slippage.
        """

        raise NotImplementedError()
