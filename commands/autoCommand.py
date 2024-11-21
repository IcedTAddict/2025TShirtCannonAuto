import commands2
import typing
from subsystems.drivetrain import arcadeDrive
from subsystems.limelight import limelightSystem

class autoCommand(commands2.CommandBase):
    def __init__(self, arcade_drive: arcadeDrive, limelight: limelightSystem) -> None:
        super().__init__()
        self.arcade_drive = arcade_drive
        self.limelight = limelight
        self.addRequirements(arcade_drive, limelight)

    def execute(self) -> None:
        res = self.limelight.get_results()

        if (res.tagId if res else 'none' != 'none'):
            match(res.tagId if res else 'none'):
                case True:
                    self.arcade_drive.arcadeDrive(0, 0.5)
                case False:
                    self.arcade_drive.arcadeDrive(0, -0.5)
                case _:
                    self.arcade_drive.arcadeDrive(0.5, 0)
        else:
            self.arcade_drive.arcadeDrive(0.5, 0)


    def isFinished(self) -> bool:
        return False
    
    def end(self) -> None:
        self.arcade_drive.arcadeDrive(0, 0)

    def isEven(self, inp) -> bool:
        if (inp % 2 == 0):
            return True
        elif (inp % 2 == 1) :
            return False