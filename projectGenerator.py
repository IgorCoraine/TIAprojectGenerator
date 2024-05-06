import clr
clr.AddReference('C:\Program Files\Siemens\Automation\Portal V18\PublicAPI\V18\Siemens.Engineering.dll')
from System.IO import DirectoryInfo, FileInfo
import Siemens.Engineering as tia
import Siemens.Engineering.HW.Features as hwf
import Siemens.Engineering.Compiler as comp
import os

#Starting TIA
print ('Starting TIA without UI')
mytia = tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)