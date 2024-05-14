# Artifact 3 - twerking robot

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
from src.MovementGroup import MovementGroups

Move = MovementGroups()

Move.look_right()
#Move.look_upperright()
#Move.look_up()
#Move.look_upperleft()
#Move.look_left()
#Move.look_leftlower()
#Move.look_down()
#Move.look_rightlower()
#Move.look_right()
#Move.stop()
#Move.move_right()
#Move.move_forward()
#Move.move_left()
#Move.move_backward()
#Move.move_right()
#Move.stop()

MovementLib = Move.MovementLib







#MovementGroup Code
import numpy as np
from src.MovementScheme import Movements 

"please comfirm the size of legs,speed,attitude all same in youe design movements"
class MovementGroups:

    def __init__(self):
        self.MovementLib = []
        self.default_stand = [[[0.06,-0.05,-0.07]],[[0.06, 0.05,-0.07]],[[-0.06,-0.05,-0.07]],[[-0.06, 0.05,-0.07]]]
 
    def stop(self):
        """Return to the default natural standing position
        Returns:
        	Append the default standing position into MovementLib
        """
        dance_scheme = Movements('stop')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]        # speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]     # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib

    def look_up(self):  
        """Set robot look up 20deg, you can change the deg parameter in this function.
        Returns:
        	Append the look up movement into MovementLib
        """    
        dance_scheme = Movements('look_up')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]       # speed_x, speed_y, no_use
        dance_attitude = [[0,20,0]]   # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)     # append dance
        return self.MovementLib
 
    def look_down(self):
        """Set robot look down 20deg, you can change the deg parameter in this function.
        Returns:
        	Append the look down movement into MovementLib
        """ 
        dance_scheme = Movements('look_down')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]       # speed_x, speed_y, no_use
        dance_attitude = [[0,-20,0]]  # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib

    def look_right(self):
        """Set robot look right 30deg, you can change the deg parameter in this function.
        Returns:
        	Append the look right movement into MovementLib
        """
        dance_scheme = Movements('look_right')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]       # speed_x, speed_y, no_use
        dance_attitude = [[0,0,30]]   # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
 
    def look_left(self):
        """Set robot look left 30deg, you can change the deg parameter in this function.
        Returns:
        	Append the look left movement into MovementLib
        """
        dance_scheme = Movements('look_left')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]       # speed_x, speed_y, no_use
        dance_attitude = [[0,0,-30]]  # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
  
    def look_upperleft(self):
        """Set robot look up 20deg and look left 30deg, you can change the deg parameter in this function.
        Returns:
        	Append the look upperleft movement into MovementLib
        """
        dance_scheme = Movements('look_upperleft')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]       # speed_x, speed_y, no_use
        dance_attitude = [[0,20,-30]] # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib

    def look_upperright(self):
        """Set robot look up 20deg and look right 30deg, you can change the deg parameter in this function.
        Returns:
        	Append the look upperright movement into MovementLib
        """
        dance_scheme = Movements('look_upperright')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]       # speed_x, speed_y, no_use
        dance_attitude = [[0,20,30]]  # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
  
    def look_rightlower(self):
        """Set robot look down 20deg and look right 30deg, you can change the deg parameter in this function.
        Returns:
        	Append the look rightlower movement into MovementLib
        """
        dance_scheme = Movements('look_rightlower')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]       # speed_x, speed_y, no_use
        dance_attitude = [[0,-20,30]] # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
  
    def look_leftlower(self):
        """Set robot look down 20deg and look left 30deg, you can change the deg parameter in this function.
        Returns:
        	Append the look leftlower movement into MovementLib
        """
        dance_scheme = Movements('look_leftlower')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0,0]]       # speed_x, speed_y, no_use
        dance_attitude = [[0,-20,-30]]# roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
                          
    def move_forward(self):
        """Set robot move forward as 0.15m/s, you can change the velocity parameter in this function.
        Returns:
        	Append the move forward movement into MovementLib
        """
        dance_scheme = Movements('move_forward')
        dance_all_legs = self.default_stand
        dance_speed = [[0.15,0,0]]    # speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]    # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
     
    def move_backward(self):
        """Set robot move backward as 0.15m/s, you can change the velocity parameter in this function.
        Returns:
        	Append the move backward movement into MovementLib
        """
        dance_scheme = Movements('move_backward')
        dance_all_legs = self.default_stand
        dance_speed = [[-0.15,0,0]]   # speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]    # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib

    def move_right(self):
        """Set robot move right as 0.15m/s, you can change the velocity parameter in this function.
        Returns:
        	Append the move right movement into MovementLib
        """
        dance_scheme = Movements('move_right')
        dance_all_legs = self.default_stand
        dance_speed = [[0,-0.15,0]]    # speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]     # roll, pitch, yaw rate
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
  
    def move_left(self):
        """Set robot move left as 0.15m/s, you can change the velocity parameter in this function.
        Returns:
        	Append the move left movement into MovementLib
        """
        dance_scheme = Movements('move_left')
        dance_all_legs = self.default_stand
        dance_speed = [[0,0.15,0]]    # speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]    # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
   
    def move_leftfront(self):
        """Set robot move leftfront as 0.15*sqrt(2)m/s, you can change the velocity parameter in this function.
        Returns:
        	Append the move leftfront movement into MovementLib
        """
        dance_scheme = Movements('move_leftfront')
        dance_all_legs = self.default_stand
        dance_speed = [[0.15,0.15,0]] # speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]    # roll, pitch, yaw rate
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
    
    def move_rightfront(self):
        """Set robot move rightfront as 0.15*sqrt(2)m/s, you can change the velocity parameter in this function.
        Returns:
        	Append the move rightfront movement into MovementLib
        """
        dance_scheme = Movements('move_rightfront')
        dance_all_legs = self.default_stand
        dance_speed = [[0.15,-0.15,0]] # speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]     # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
    
    def move_leftback(self):
        """Set robot move leftback as 0.15*sqrt(2)m/s, you can change the velocity parameter in this function.
        Returns:
        	Append the move leftback movement into MovementLib
        """
        dance_scheme = Movements('move_leftback')
        dance_all_legs = self.default_stand
        dance_speed = [[-0.15,0.15,0]]# speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]    # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
 
    def move_rightback(self):
        """Set robot move rightback as 0.15*sqrt(2)m/s, you can change the velocity parameter in this function.
        Returns:
        	Append the move rightback movement into MovementLib
        """
        dance_scheme = Movements('move_rightback')
        dance_all_legs = self.default_stand
        dance_speed = [[-0.15,-0.15,0]]# speed_x, speed_y, no_use
        dance_attitude = [[0,0,0]]     # roll, pitch, yaw rate
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance
        return self.MovementLib
        
      
"""  
    #multiple move in one movement example1
    #it is a series of movement,keep down first then back to default stand ,move forward ,finally stop  
    def down_trot(self):    
        dance_scheme = Movements('down_trot')

        dance_all_legs = []
        dance_all_legs.append([[ 0.06,-0.05,-0.07],[ 0.06,-0.05,-0.04],[ 0.06,-0.05,-0.07],[ 0.06,-0.05,-0.07],[ 0.06,-0.05,-0.07]]) #leg1
        dance_all_legs.append([[ 0.06, 0.05,-0.07],[ 0.06, 0.05,-0.04],[ 0.06, 0.05,-0.07],[ 0.06, 0.05,-0.07],[ 0.06, 0.05,-0.07]]) #leg2
        dance_all_legs.append([[-0.06,-0.05,-0.07],[-0.06,-0.05,-0.04],[-0.06,-0.05,-0.07],[-0.06,-0.05,-0.07],[-0.06,-0.05,-0.07]]) #leg3
        dance_all_legs.append([[-0.06, 0.05,-0.07],[-0.06, 0.05,-0.04],[-0.06, 0.05,-0.07],[-0.06, 0.05,-0.07],[-0.06, 0.05,-0.07]]) #leg4

        dance_speed = [[0,0,0],[0,0,0],[0,0,0],[0.15,0,0],[0,0,0]]    # speed_x, speed_y, no_use

        dance_attitude = [[0,0,0],[10,0,0],[0,0,0],[0,0,0],[0,0,0]]   # roll, pitch, yaw degree
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)

        return self.MovementLib

    #multiple move in one movement example2  
    #it is a series of movement,keep up first then back to default stand ,move forward ,finally stop
    def up_trot(self):    
        dance_scheme = Movements('up_trot')

        dance_all_legs = []
        dance_all_legs.append([[ 0.06,-0.05,-0.07],[ 0.06,-0.05,-0.10],[ 0.06,-0.05,-0.07],[ 0.06,-0.05,-0.07],[ 0.06,-0.05,-0.07]])# leg1
        dance_all_legs.append([[ 0.06, 0.05,-0.07],[ 0.06, 0.05,-0.10],[ 0.06, 0.05,-0.07],[ 0.06, 0.05,-0.07],[ 0.06, 0.05,-0.07]])# leg2
        dance_all_legs.append([[-0.06,-0.05,-0.07],[-0.06,-0.05,-0.10],[-0.06,-0.05,-0.07],[-0.06,-0.05,-0.07],[-0.06,-0.05,-0.07]])# leg3
        dance_all_legs.append([[-0.06, 0.05,-0.07],[-0.06, 0.05,-0.10],[-0.06, 0.05,-0.07],[-0.06, 0.05,-0.07],[-0.06, 0.05,-0.07]])# leg4

        dance_speed = [[0,0,0],[0,0,0],[0,0,0],[0.1,0,0],[0,0,0]]    # speed_, speed_y, no_use

        dance_attitude = [[0,0,0],[10,0,0],[0,0,0],[0,0,0],[0,0,0]]  # roll, pitch, yaw rate
        dance_scheme.setAllSequence(dance_all_legs,dance_speed,dance_attitude)
        self.MovementLib.append(dance_scheme)      # append dance

        return self.MovementLib
"""











#MovementScheme Code

import numpy as np

LocationStanding = [[ 0.06,0.06,-0.06,-0.06],[-0.05, 0.05,-0.05,0.05],[ -0.07,-0.07,-0.07,-0.07]]
SpeedStanding = [0,0,0]
AttitudeStanding = [0,0,0]

DeltLocationMax = 0.0005 #unit m
DeltSpeedMax = 0.0025 #unit m/s
DeltAttitudeMax = 1 #unit degree

AttitudeMinMax = [[-20,20],[-20,20],[-60,60]]

class SequenceInterpolation:
    """
    this class used to set sequence interpolation, such as legs_location,speed and attitude
    """
    def __init__(self,name,dimension):
        self.Name = name
        self.Dimension = dimension
        # default value is 70
        self.InterpolationNumber = 70

        self.ExecuteTick = 0
        self.SequenceExecuteCounter = 0
        self.PhaseNumberMax = 1
        self.SequencePoint = [[0,0,0]]

        # interpolation point data 
        self.PointPhaseStart = 0
        self.PointPhaseStop = 1
        self.TnterpolationDelt = [0,0,0]
        self.PointNow = [0,0,0]                 
        self.PointPrevious = [0,0,0]

    def setCycleType(self,cycle_type,cycle_index):
        """set cycle type ,include Forever , Multiple, or single,the cycle_index is the loop times
        
        parameter: cycle_type,cycle_index
        """
        if cycle_type == 'Forever':
            self.SequenceExecuteCounter = 9999
        elif cycle_type == 'Multiple':
            self.SequenceExecuteCounter = cycle_index
        else:
            self.SequenceExecuteCounter = 1  

        return True
        
    def setInterpolationNumber(self,interpolation_number):
        self.InterpolationNumber = interpolation_number
        return True
        
    def setSequencePoint(self,sequence):
        """this function is to init the sequence
        
        Parameters: sequence
        ---------  
        Returns: True
        """
        self.SequencePoint = sequence
        self.PhaseNumberMax = len(sequence)
        
        # init now and pre point phase
        for xyz in range(self.Dimension):
        
            self.PointNow[xyz] = sequence[0][xyz] 
            self.PointPrevious[xyz] = sequence[0][xyz] 
            
        # init start point phase
        self.PointPhaseStart  = 0
        # init stop point phase
        self.PointPhaseStop  = self.PointPhaseStart + 1
        if self.PointPhaseStop >= len(sequence):
            self.PointPhaseStop = self.PointPhaseStart
        #init the first diff
        point_start = sequence[self.PointPhaseStart]
        point_stop = sequence[self.PointPhaseStop]
        
        for xyz in range(self.Dimension):
            
            diff =   point_stop[xyz] - point_start[xyz]
              
            self.TnterpolationDelt[xyz] = diff/self.InterpolationNumber

        return True

    def updatePointPhase(self):
        """this function is to update the point phase ,include start phase and stop phase
        
        Parameters: Null
        ---------  
        Returns: True
        """
        # update start point phase
        self.PointPhaseStart  = self.PointPhaseStart + 1
        if self.PointPhaseStart >= self.PhaseNumberMax:
            if self.SequenceExecuteCounter >0:
                self.PointPhaseStart = 0
            else:
                self.SequenceExecuteCounter = 0
                self.PointPhaseStart = self.PointPhaseStart - 1

        # update stop point phase
        self.PointPhaseStop  = self.PointPhaseStart + 1
        if self.PointPhaseStop >= self.PhaseNumberMax:
            self.SequenceExecuteCounter = self.SequenceExecuteCounter - 1
            if self.SequenceExecuteCounter >0:
                self.PointPhaseStop = 0
            else:
                self.SequenceExecuteCounter = 0
                self.PointPhaseStop = self.PointPhaseStop - 1
            
        return True

    def updateInterpolationDelt(self):
        """this function is to update the delt about new start phase and new stop phase
        
        Parameters: Null
        ---------  
        Returns: True
        """
        #get start and stop point
        point_start  = self.SequencePoint[self.PointPhaseStart]
        point_stop  = self.SequencePoint[self.PointPhaseStop]
                        
        for xyz in range(self.Dimension):
                
            diff =   point_stop[xyz] - point_start[xyz]
              
            self.TnterpolationDelt[xyz] = diff/self.InterpolationNumber
                
        return True
                
    def getNewPoint(self):
        """this function is to get new value in the next interpolation point
        
        Parameters: Null
        ---------  
        Returns: self.pointnow, the new value of the new point 
        """
        #update movement tick
        self.ExecuteTick = self.ExecuteTick + 1
        if self.ExecuteTick > self.InterpolationNumber:
             self.ExecuteTick = 0
             self.updatePointPhase()
             self.updateInterpolationDelt()
        else:
            self.PointNow[0] = self.PointPrevious[0] + self.TnterpolationDelt[0]
            self.PointNow[1] = self.PointPrevious[1] + self.TnterpolationDelt[1]
            self.PointNow[2] = self.PointPrevious[2] + self.TnterpolationDelt[2]
            self.PointPrevious = self.PointNow

        return self.PointNow

class Movements:
    """this class used to set three interpolation of movement through the first class called sequenceInterpolation
       legs_location,speed and sttitude
    """
    def __init__(self,name,speed_enable = "SpeedEnable",attitude_enable = "AttitudeEnable",legs_enable = "LegsEnable"):

        self.MovementName =  name

        self.SpeedEnable = speed_enable
        self.AttitudeEnable = attitude_enable
        self.LegsEnable = legs_enable
        self.ExitToStand = False

        self.SpeedMovements = SequenceInterpolation('speed',2)
        self.AttitudeMovements = SequenceInterpolation('attitude',3)
        self.LegsMovements = []
        self.LegsMovements.append(SequenceInterpolation('leg1',3))
        self.LegsMovements.append(SequenceInterpolation('leg2',3))
        self.LegsMovements.append(SequenceInterpolation('leg3',3))
        self.LegsMovements.append(SequenceInterpolation('leg4',3))

        # init state value
        self.SpeedInit = [0,0,0]          # x, y speed
        self.AttitudeInit = [0,0,0]     # roll pitch yaw rate
        self.LegsLocationInit = [[0,0,0,0],[0,0,0,0],[0,0,0,0]] # x,y,z for 4 legs

        # output
        self.SpeedOutput = [0,0,0]          # x, y speed
        self.AttitudeOutput = [0,0,0]     # roll pitch yaw rate
        self.LegsLocationOutput = [[0,0,0,0],[0,0,0,0],[0,0,0,0]] # x,y,z for 4 legs

    def setInterpolationNumber(self,number):
        """set interpolation number for three parts
        """    
        for leg in range(4):
            self.LegsMovements[leg].setInterpolationNumber(number)  
        self.AttitudeMovements.setInterpolationNumber(number)  
        self.SpeedMovements.setInterpolationNumber(number)  
        return True
        
    def setExitstate(self,state = "Continue"):
        """set exit state ,Stand is keep Stand after this move,Continue is keep this movement after this movement
        """
        if state == 'Stand':
            self.ExitToStand = True
        return True
        
    def setSpeedSequence(self,sequence,cycle_type = "single",cycle_index = 1):
        """set speed sequence

        Args:
            sequence (_type_): your design movement in speed part
            cycle_type (str, optional): three type :Forever, Multiple,single. Defaults to "single".
            cycle_index (int, optional): just can be set in Multiple type. Defaults to 1.
        """
        self.SpeedMovements.setSequencePoint(sequence)
        self.SpeedMovements.setCycleType(cycle_type,cycle_index)
        self.SpeedInit = sequence[0]


    def setAttitudeSequence(self,sequence,cycle_type = "single",cycle_index = 1):
        """set speed sequence

        Args:
            sequence (_type_): your design movement in attitude part
            cycle_type (str, optional): three type :Forever, Multiple,single. Defaults to "single".
            cycle_index (int, optional): just can be set in Multiple type. Defaults to 1.
        """
        self.AttitudeMovements.setSequencePoint(sequence)
        self.AttitudeMovements.setCycleType(cycle_type,cycle_index)
        self.AttitudeInit = sequence[0]

    def setLegsSequence(self,sequence,cycle_type = "single",cycle_index = 1):
        """set four legs sequence

        Args:
            sequence (_type_): your design movement in legs_location part
            cycle_type (str, optional): three type :Forever, Multiple,single. Defaults to "single".
            cycle_index (int, optional): just can be set in Multiple type. Defaults to 1.
        """
        for leg in range(4):
            self.LegsMovements[leg].setSequencePoint(sequence[leg])
            self.LegsMovements[leg].setCycleType(cycle_type,cycle_index)
            
            # init location
            self.LegsLocationInit[0][leg] = sequence[leg][0][0]
            self.LegsLocationInit[1][leg] = sequence[leg][0][1]
            self.LegsLocationInit[2][leg] = sequence[leg][0][2]

    def setAllSequence(self,sequenceLeg,sequenceSpeed,sequenceAttitude):
        """for less code in danceSample
           you can through this function to set three part sequence interpolation when this parts type all is "single"
        """
        Movements.setLegsSequence(self,sequenceLeg)
        Movements.setSpeedSequence(self,sequenceSpeed)
        Movements.setAttitudeSequence(self,sequenceAttitude)
    

    def runMovementSequence(self):
        """you can set three parts state if Enable it will caculate the new interpolation point value, else will not
        """
        if self.SpeedEnable == 'SpeedEnable':
            self.SpeedOutput = self.SpeedMovements.getNewPoint()

        if self.AttitudeEnable == 'AttitudeEnable':
            self.AttitudeOutput = self.AttitudeMovements.getNewPoint()

        if self.LegsEnable == 'LegsEnable':
            for leg in range(4):
                leg_loaction = self.LegsMovements[leg].getNewPoint()
                for xyz in range(3):
                    self.LegsLocationOutput[xyz][leg] = leg_loaction[xyz]


    def getSpeedOutput(self, state = 'Normal'):
        """get every interpolation point value of speed
        """
        if state == 'Init':
            return self.SpeedInit
        else:
            return self.SpeedOutput

    def getAttitudeOutput(self, state = 'Normal'):
        """get every interpolation point value of attitude
        """
        if state == 'Init':
            return self.AttitudeInit
        else:
            return self.AttitudeOutput

    def getLegsLocationOutput(self, state = 'Normal'):
        """get every interpolation point value of legs_location
        """
        if state == 'Init':
            return self.LegsLocationInit
        else:
            return self.LegsLocationOutput

    def getMovementName(self):
        """
        Returns:
            string : MovementName 
        """
        return self.MovementName
           
    def getCycleTicks(self):
        """the cycle ticks is the total number of interpolation in one movement 

        Returns:
        number
        """
        return (self.SpeedMovements.PhaseNumberMax - 1)* self.SpeedMovements.InterpolationNumber*self.SpeedMovements.SequenceExecuteCounter
        
    def getPhaseNumberMax(self):
        """
        Returns:
        the phase number in one movement
        """
        return self.SpeedMovements.PhaseNumberMax

class MovementScheme:
    """this class is to contact two movement,finally you can through this class to get a movementlib which have a series of movement 
    """
    def __init__(self,movements_lib):

        self.movements_lib = movements_lib
        
        self.movements_now = movements_lib[0]
        self.movements_pre = movements_lib[0]
        self.movement_now_name =  movements_lib[0].getMovementName()
        self.movement_now_number = 0
        self.transition = False
        
        self.ststus = 'Movement'    # 'Entry' 'Movement' 'Exit'
        self.entry_down = False
        self.entry_down1 = False
        self.entry_down2 = False
        self.exit_down = False
        self.exit_down1 = False
        self.exit_down2 = False
        self.tick = 0
        self.Legslocation_gradient_done_counter = 0
        self.Speed_gradient_done_counter = 0
        self.Attitude_gradient_done_counter = 0

        self.legs_location_pre = LocationStanding
        self.legs_location_now = LocationStanding
        self.speed_pre = SpeedStanding
        self.speed_now = SpeedStanding
        self.attitude_pre = AttitudeStanding
        self.attitude_now = AttitudeStanding
        
        self.legslocation_done_index = np.zeros((3,4))
        self.speed_done_index = [0,0,0]
        self.attitude_done_index = [0,0,0]
        
        self.legslocation_gradient_done = False
        self.speed_gradient_done = False
        self.attitude_gradient_done = False

        self.attitude_pre = [0,0,0]
        self.attitude_now = [0,0,0]

        self.speed_pre = [0,0,0]
        self.speed_now = [0,0,0]
        
        self.record_index_number = [] 

    def updateMovementType(self):
        """used to update movement ,caculate which movement should be move

        Returns:
            string : the new movement name
        """
        self.movements_pre = self.movements_lib[self.movement_now_number]
        self.movement_now_number = self.movement_now_number + 1
        if self.movement_now_number>= len(self.movements_lib):
            self.movement_now_number = self.movement_now_number - 1 
        self.entry_down = False
        self.entry_down1 = False
        self.entry_down2 = False
        self.exit_down = False
        self.exit_down1 = False
        self.exit_down2 = False
        self.transition = False
        self.movements_now = self.movements_lib[self.movement_now_number]

        return self.movements_now.getMovementName()

    def resetMovementNumber(self):
        """reset the movement ,let the action move from first movement

        """
        self.movements_pre = self.movements_lib[self.movement_now_number]
        self.movement_now_number = 0
        
        self.entry_down = False
        self.entry_down1 = False
        self.entry_down2 = False
        
        self.exit_down = False
        self.exit_down1 = False
        self.exit_down2 = False
        self.movements_now = self.movements_lib[0]

        return True
    
    def updateMovement(self,movement_type):
        """update movement, when the state is "entry",there will caculate the gradient about three parts(legs_location,speed,attitude) 
           when transition between two movement

        Args:
            movement_type (string): the name of the movement
        """
        # movement state transition
        if (movement_type != self.movement_now_name):
            self.ststus = 'Exit'
        elif(self.entry_down and self.entry_down1 and self.entry_down2):
            self.ststus = 'Movement'
        elif(self.exit_down and self.exit_down1 and self.exit_down2):
            self.ststus = 'Entry'
        
        
        self.movement_now_name = movement_type
        now_ticks = self.movements_now.getCycleTicks()

        # update system tick
        
        # movement execute
        if self.ststus == 'Entry':
        #this part is superimposed model
#             if self.movements_now.getMovementName() == 'stop':
#             
#                 self.record_index_number = []
#                 location_ready = self.movements_now.getLegsLocationOutput('Init')
#                 speed_ready = self.movements_now.getSpeedOutput('Init')
#                 attitude_ready = self.movements_now.getAttitudeOutput('Init')
#                 
#             else:
#
#                 location_ready = np.array(self.movements_now.getLegsLocationOutput('Init'))
#                 speed_ready = np.array(self.movements_now.getSpeedOutput('Init'))
#                 attitude_ready = np.array(self.movements_now.getAttitudeOutput('Init'))
#                 
#                 if (self.movement_now_number - 1) not in self.record_index_number: 
#                     self.record_index_number.append(self.movement_now_number - 1)
#                 print("movement_now_number",self.movement_now_number)
#                 for number_index in range(len(self.record_index_number)):
#                     print("record_index_number",self.record_index_number)
#                     speed_ready = np.array(speed_ready) + np.array(self.movements_lib[self.record_index_number[number_index]].getSpeedOutput('Init'))
#                     attitude_ready = np.array(attitude_ready) + np.array(self.movements_lib[self.record_index_number[number_index]].getAttitudeOutput('Init'))

             location_ready = np.array(self.movements_now.getLegsLocationOutput('Init'))
             speed_ready = np.array(self.movements_now.getSpeedOutput('Init'))
             attitude_ready = np.array(self.movements_now.getAttitudeOutput('Init'))
             
             self.legs_location_now, self.entry_down = self.updateMovementLegsLocationGradient(self.legs_location_pre,location_ready)
             self.legs_location_pre = self.legs_location_now
             
             self.speed_now, self.entry_down1 = self.updateMovementSpeedGradient(self.speed_pre,speed_ready)
             self.speed_pre = self.speed_now
             
             self.attitude_now, self.entry_down2 = self.updateMovementAttitudeGradient(self.attitude_pre,attitude_ready)
             self.attitude_pre = self.attitude_now
             
             if self.entry_down == True and self.entry_down1 == True and self.entry_down2 == True:
             
                 self.Legslocation_gradient_done_counter = 0
                 self.speed_gradient_done_counter = 0
                 self.attitude_gradient_done_counter = 0
                 
                 self.exit_down = False
                 self.exit_down1 = False
                 self.exit_down2 = False
                 self.legslocation_gradient_done = False
                 self.speed_gradient_done = False
                 self.attitude_gradient_done = False
                 
                 self.legslocation_done_index = np.zeros((3,4))
                 self.speed_done_index = [0,0]
                 self.attitude_done_index = [0,0,0]

        if self.ststus == 'Exit':
             if self.movements_pre.ExitToStand == True:
                  #update the legslocation
                  self.legs_location_now, self.exit_down=self.updateMovementLegsLocationGradient(self.legs_location_pre,LocationStanding)
                  self.legs_location_pre = self.legs_location_now
                  
                  #update the speed
                  self.speed_now, self.exit_down1=self.updateMovementSpeedGradient(self.speed_pre,SpeedStanding)
                  self.legs_location_pre = self.legs_location_now
                  
                  #update the attitude
                  self.attitude_now, self.exit_down2=self.updateMovementAttitudeGradient(self.attitude_pre,AttitudeStanding)
                  self.attitude_pre = self.attitude_now
                  
                  if self.exit_down == True and self.exit_down1 == True and self.exit_down2 == True:
                  
                      self.Legslocation_gradient_done_counter = 0
                      self.Speed_gradient_done_counter = 0
                      self.Attitude_gradient_done_counter = 0
                      
                      self.legslocation_done_index = np.zeros((3,4))
                      self.speed_done_index = [0,0]
                      self.attitude_done_index = [0,0,0]
                      
                      self.entry_down = False
                      self.entry_down1 = False
                      self.entry_down2 = False
                      self.legslocation_gradient_done = False
                      self.speed_gradient_done = False
                      self.attitude_gradient_done = False
                      
             else:
                  self.legs_location_now = self.legs_location_pre
                  self.speed_now = self.speed_pre
                  self.attitude_now = self.attitude_pre
                  self.exit_down = True
                  self.exit_down1 = True
                  self.exit_down2 = True
                  self.entry_down = False
                  self.entry_down1 = False
                  self.entry_down2 = False
                  self.legslocation_gradient_done = False
                  self.speed_gradient_done = False
                  self.attitude_gradient_done = False
                  self.Legslocation_gradient_done_counter = 0
                  self.Speed_gradient_done_counter = 0
                  self.Attitude_gradient_done_counter = 0


        elif self.ststus == 'Movement':
             if self.movements_now.getPhaseNumberMax() > 1 :
                 self.updateMovemenScheme()

             self.legs_location_pre = self.legs_location_now
             self.speed_pre = self.speed_now 
             self.attitude_pre = self.attitude_now
             
             self.tick += 1
             if self.tick >= now_ticks  and self.movement_now_number < len(self.movements_lib) - 1:
                 self.transition = True
                 self.tick = 0

        return self.legs_location_now,self.speed_now,self.attitude_now

    def updateMovementLegsLocationGradient(self,location_now,location_target):
        """uodate gradient legs_locaiton between two movement

        Args:
            location_now (array 3*4): now legs_location
            location_target (arrar 3*4): target legs_location

        Returns:
        location_gradient: new legs_locaiton in transition
        self.legslocation_gradient_done: the state about legs_locaiton transition
        """
        loaction_gradient = location_now

        #legs gradient
        for xyz_index in range(3):
            for leg_index in range(4):

                diff = location_target[xyz_index][leg_index] - location_now[xyz_index][leg_index]
                if diff > DeltLocationMax:
                    loaction_gradient[xyz_index][leg_index] = location_now[xyz_index][leg_index] + DeltLocationMax
                elif diff < -DeltLocationMax:
                    loaction_gradient[xyz_index][leg_index] = location_now[xyz_index][leg_index] - DeltLocationMax                
                else :
                    loaction_gradient[xyz_index][leg_index] = location_target[xyz_index][leg_index]
                    if self.legslocation_done_index[xyz_index][leg_index] != 1:
                        self.Legslocation_gradient_done_counter += 1
                        self.legslocation_done_index[xyz_index][leg_index] = 1
                    
        if self.Legslocation_gradient_done_counter == 12:
            
            self.legslocation_gradient_done = True

        return loaction_gradient,self.legslocation_gradient_done
        
    def updateMovementSpeedGradient(self,speed_now,speed_target):
        """uodate gradient speed between two movement

        Args:
            speed_now (array 1*3): now speed
            speed_target (arrar 1*3): target speed

        Returns:
        speed_gradient: new speed in transition
        self.speed_gradient_done: the state about speed transition
        """
        speed_gradient = speed_now
        gradient_done = False

        #speed gradient
        for xy_index in range(2):
                diff = speed_target[xy_index] - speed_now[xy_index]
                if diff > DeltSpeedMax:
                    speed_gradient[xy_index] = speed_now[xy_index] + DeltSpeedMax
                elif diff < -DeltSpeedMax:
                    speed_gradient[xy_index] = speed_now[xy_index] - DeltSpeedMax                
                else :
                    speed_gradient[xy_index] = speed_target[xy_index]
                    if self.speed_done_index[xy_index] != 1 :
                        self.speed_done_index[xy_index] = 1
                        self.Speed_gradient_done_counter += 1
                    
        if self.Speed_gradient_done_counter == 2:
            
            self.speed_gradient_done = True

        return speed_gradient,self.speed_gradient_done

    def updateMovementAttitudeGradient(self,attitude_now,attitude_target):
        """uodate gradient attitude between two movement

        Args:
            attitude_now (array 1*3): now attitude
            attitude_target (arrar 1*3): target attitude

        Returns:
        attitude_gradient: new attitude in transition
        self.attitude_gradient_done: the state about attitude transition
        """
        attitude_gradient = attitude_now
        #Attitude gradient
        for rpy_index in range(3):
                diff = attitude_target[rpy_index] - attitude_now[rpy_index]
                if diff > DeltAttitudeMax:
                    attitude_gradient[rpy_index] = attitude_now[rpy_index] + DeltAttitudeMax
                elif diff < -DeltAttitudeMax:
                    attitude_gradient[rpy_index] = attitude_now[rpy_index] - DeltAttitudeMax                
                else :
                    attitude_gradient[rpy_index] = attitude_target[rpy_index]
                    if self.attitude_done_index[rpy_index] != 1 :
                        self.Attitude_gradient_done_counter += 1
                        self.attitude_done_index[rpy_index] = 1
                    
        if self.Attitude_gradient_done_counter == 3:
            
            self.attitude_gradient_done = True

        return attitude_gradient,self.attitude_gradient_done
        
        
    def updateMovemenScheme(self):
        """this function used to update the value of three parts
        """
        # run movement
        self.movements_now.runMovementSequence()

        # legs movement
        self.legs_location_now = self.movements_now.getLegsLocationOutput('normal')
        # speed movement
        self.speed_now = self.movements_now.getSpeedOutput('normal')
        # attitude movement
        self.attitude_now = self.movements_now.getAttitudeOutput('normal')
        
        for rpy in range(3):

            #limite attitude angle
            if self.attitude_now[rpy] < AttitudeMinMax[rpy][0]:
                self.attitude_now[rpy] = AttitudeMinMax[rpy][0]
            elif self.attitude_now[rpy] > AttitudeMinMax[rpy][1]:
                self.attitude_now[rpy] = AttitudeMinMax[rpy][1]

        return  True

    def runMovementScheme(self):
        """run the movement in movementlib
        """
        # update movement
        movement_name = ' '
        if self.transition == True:
            movement_name = self.updateMovementType()

        self.updateMovement(movement_name) 
 
        return True

    def getMovemenSpeed(self):
        """get now speed
        """
        speed_now = [0,0,0]
        for xyz in range(3):

            speed_now[xyz] = self.speed_now[xyz]
        return speed_now

    def getMovemenLegsLocation(self):
        """get now legs_location
        """
        return self.legs_location_now 

    def getMovemenAttitude(self):
        """get now attitude
        """
        attitude_now_rad = [0,0,0] 

        for rpy in range(3):
            #angle to radin
            attitude_now_rad[rpy] = self.attitude_now[rpy] / 57.3

        return   attitude_now_rad

