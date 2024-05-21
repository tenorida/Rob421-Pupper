#
# Copyright 2024 MangDang (www.mangdang.net) 
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
#
# Test method1: use controller to do your designed movements 
#   step1: Pair the controller to your Mini Pupper
#   step2: Click controller "L1" button
#   step3: Click controller "Circle" button 
#   the mini pupper will dance based on your following script.
#
#
#Test method2: run dancemove.py to do your designed movements
#   method: type the following command line:
#           python /home/ubuntu/StanfordQuadruped/dancemove.py
#
#
# Movement Action API List without input parameters
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
# Movement Action API List wit input parameters
# body_row(row_deg,  time_uni, time_acc)
# gait_uni(v_x, v_y, time_uni, time_acc)
# height_move(ht,    time_uni, time_acc)
# head_move(pitch_deg, yaw_deg, time_uni, time_acc)
# foreleg_lift(leg_index, ht,   time_uni, time_acc)
# backleg_lift(leg_index, ht,   time_uni, time_acc)
# 

from MovementGroup_updated import MovementGroups

Move = MovementGroups()

# movements without input parameters
Move.look_right()
print("why work?")
Move.look_upperright()
Move.look_up()
Move.look_upperleft()
Move.look_left()
Move.look_leftlower()
Move.look_down()
Move.look_rightlower()
Move.look_right()
Move.stop()
Move.move_right()
Move.move_forward()
Move.move_left()
Move.move_backward()
Move.move_right()
Move.stop()

# movements with input parameters
Move.head_move(20)
print("don't wanna")
Move.stop()
Move.body_row(10)
Move.body_row(-10)
Move.stop()
Move.gait_uni(0.25,0)
Move.gait_uni(0.35, 0.1)
Move.stop()
Move.height_move(0.03)
Move.height_move(-0.02)
Move.stop()
Move.gait_uni(0.1)
Move.stop()


MovementLib = Move.MovementLib
