import clr
clr.AddReference('C:\Program Files\Siemens\Automation\Portal V18\PublicAPI\V18\Siemens.Engineering.dll')
from System.IO import DirectoryInfo, FileInfo
import Siemens.Engineering as tia
import Siemens.Engineering.HW.Features as hwf
import Siemens.Engineering.Compiler as comp
import os
from device import Device


class TIAProject:
    def __init__(self):
        self.tia_instance = None
        self.project = None

    def startTIA(self, ui: bool):
        self.tia_instance = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface) if ui else tia.TiaPortal(tia.TiaPortalMode.WithoutUserInterface)

    def generate_project_name(self, project_path, project_name):
        _project_name = project_name
        count = 1
        while os.path.exists(f'{project_path}\\{_project_name}'):
            _project_name = f"{project_name}({count})"
            count += 1
        return _project_name
    
    def create_project(self, project_path, project_name):
        self.project = self.tia_instance.Projects.Create(DirectoryInfo(project_path), self.generate_project_name(project_path, project_name))
        
    #Adding the main components
    def create_device(self, name: str, device: str, version: float):
        try:
            print (f'Creating {device}/V{version}')
            PLC1_mlfb = f'OrderNumber:{device}/V{version}'
            return self.project.Devices.CreateWithItem(PLC1_mlfb, name, name)
        
        except tia.EngineeringTargetInvocationException:
            print('invalid version')
            version -= 0.1
            return self.create_device(name, device, round(version,1))

    #Plugging modules to devices
    def plug_device(self, device: Device, module: int):
        if (device.instance.DeviceItems[0].CanPlugNew(f'OrderNumber:{device.modules[module]}',f'IO{module}', module)): 
            device.instance.DeviceItems[0].PlugNew(f'OrderNumber:{device.modules[module]}',f'IO{module}', module)


    #PLC1 = create_device('PLC1', '6ES7 518-4FP00-0AB0', 10.0)


    #self.project.Save()