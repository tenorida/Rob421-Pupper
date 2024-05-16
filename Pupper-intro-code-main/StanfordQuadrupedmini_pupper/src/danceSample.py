#
# Copyright 2023 MangDang (www.mangdang.net) 
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
#
# Description: You can use the following FPC(Flexible Programmable Choreography) APIs to define your Mini Pupper to dance.
# Test method: 
#   step1: Pair the controller to your Mini Pupper
#   step2: Click controller "L1" button
#   step3: Click controller "Circle" button 
#   the mini pupper will dance based on your following script.
# stop()
# look_up()
# look_down()
# look_right()
# look_left()
# look_upperleft()
# look_upperright()
# look_rightlower()
# look_leftlower()
# move_forward()
# move_backward()
# move_right()
# move_left()
# move_leftfront()
# move_rightfront()
# move_leftback()
# move_rightback()
#

from UDPComms import Publisher
import time
from MovementGroup import MovementGroups
from movement_commands_dance import trot
#Move = MovementGroups()

trot()
time.sleep(0.2)
MovementGroups.look_right()
MovementGroups.look_upperright()
MovementGroups.look_up()
MovementGroups.look_upperleft()
MovementGroups.look_left()
MovementGroups.look_leftlower()
MovementGroups.look_down()
MovementGroups.look_rightlower()
MovementGroups.look_right()
MovementGroups.stop()
MovementGroups.move_right()
MovementGroups.move_forward()
MovementGroups.move_left()
MovementGroups.move_backward()
MovementGroups.move_right()
MovementGroups.stop()

MovementLib = Move.MovementLib
