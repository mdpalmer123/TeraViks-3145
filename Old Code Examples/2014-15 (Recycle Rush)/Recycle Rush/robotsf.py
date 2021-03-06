#Seiji Furukawa

#Libraries
import wpilib
import time
import math

#Global Variables

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.robot_drive = wpilib.RobotDrive(0,1,2,3)

        self.stick = wpilib.Joystick(0)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)    #Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

        magnitude = 0.0000000000
        magnitude = math.sqrt(self.stick.getMagnitude())

        if magnitude >= 0.6:
          #self.robot_drive.setInvertedMotor(1, True)
          #self.robot_drive.setInvertedMotor(3, True)
          self.robot_drive.holonomicDrive(magnitude-0.6, self.stick.getDirectionDegrees(), self.stick.getTwist())
        print("Magnitude: ", self.stick.getMagnitude())
        print("Magmod: ", magnitude)
        print("Direction: ", self.stick.getDirectionDegrees())
        print("Rotation: ", self.stick.getTwist())
    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
