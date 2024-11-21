import constants

import commands2
import commands2.button

import wpilib

from subsystems.drivetrain import arcadeDrive
from commands.arcadedrive import ArcadeDrive

from subsystems.limelight import limelightSystem
from commands.limelightdisplay import limelightDisplay

import commands.autoCommand


class RobotContainer:
    def __init__(self) -> None:
        self.limelight = limelightSystem()
        self.drive = arcadeDrive()
        self.stick = wpilib.Joystick(constants.DRIVE_JOYSTICK_PORT)
        self.configureButtonBindings()

        self.auto = autoCommand(self.drive, self.limelight)

    def getAutonomousCommand(self) -> commands2.Command:
        return self.auto

    def configureButtonBindings(self) -> None:
        # self.drivetrain.setDefaultCommand(ArcadeDrive(self.drivetrain, lambda: self.stick.getX(), lambda: self.stick.getY()))
        self.limelight.setDefaultCommand(limelightDisplay(self.limelight))