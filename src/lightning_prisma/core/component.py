# Copyright Justin R. Goheen.
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

import abc
import asyncio
from prisma import Prisma
from lightning import LightningWork


class LightningPrisma(LightningWork, abc.ABC):
    "a synchronous Prisma client"

    def __init__(self):
        super().__init__()
        self.prisma = Prisma()

    def connect_prisma(self):
        self.prisma.connect()

    def disconnect_prisma(self):
        self.prisma.disconnect()

    def run(self):
        self.connect_prisma()

        # write queries here

        self.disconnect_prisma()
