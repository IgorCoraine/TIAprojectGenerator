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
# Alternative code to connect to an allready running instance (uncomment to use)

#processes = tia.TiaPortal.GetProcesses() # Making a list of all running processes
#print (processes)
#process = processes[0]                   # Just taking the first process as an example
#mytia = process.Attach()
#myproject = mytia.Projects[0]

#Create a new project
project_path = DirectoryInfo ('C:\\Users\\Cassioli\\Desktop\\')
project_name = 'PythonTest'

def generate_project_name(project_path, project_name):
    _project_name = project_name
    count = 1

    while os.path.exists(f'{project_path}\\{_project_name}'):
        _project_name = f"{project_name}({count})"
        count += 1
    return _project_name

print(generate_project_name(project_path, project_name))

try:
    myproject = mytia.Projects.Create(project_path, generate_project_name(project_path, project_name))
except Exception as e:
    print (e)

#Adding the main components
def create_device(name: str, device: str, version: float):
    try:
        print (f'Creating {device}/V{version}')
        PLC1_mlfb = f'OrderNumber:{device}/V{version}'
        return myproject.Devices.CreateWithItem(PLC1_mlfb, name, name)
    
    except:
        print('invalid version')
        version -= 0.1
        create_device(name, device, round(version,1))


PLC1 = create_device('PLC1', '6ES7 518-4FP00-0AB0', 10.0)



myproject.Save()


