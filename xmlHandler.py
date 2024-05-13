import xml.etree.ElementTree as ET
from device import Device

# Função para extrair informações de dispositivos e módulos
def extract_info(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    devices = []
    current_device = None

    for node in root.findall(".//n"):
        node_type = node.get("Type")

        if node_type == "Device":
            # Se encontrarmos um novo dispositivo, criamos uma nova lista
            if current_device:
                devices.append(current_device)
            current_device = Device(node.get("Name"))
            #current_device = {"Name": node.get("Name"), "Modules": []}
        elif node_type == "Module" and current_device:
            # Adicionamos o Mlfb do módulo ao dispositivo atual
            #current_device["Modules"].append(node.get("Mlfb"))
            current_device.add_module(node.get("Mlfb"))

    # Adicionamos o último dispositivo à lista
    if current_device:
        devices.append(current_device)

    return devices

# # Caminho para o arquivo XML
# xml_file_path = "C:\\Users\\Cassioli\\Desktop\\my.xml"

# # Extrair informações do arquivo XML
# device_info = extract_info(xml_file_path)

# # Imprimir as informações dos dispositivos e módulos
# for idx, device in enumerate(device_info, start=1):
#     print(f"Device {idx}:")
#     print(f"Name: {device['Name']}")
#     print("Modules:")
#     for module in device["Modules"]:
#         print(f"- {module}")
#     print()

    
