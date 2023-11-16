# VirtualMachineVgpuDeviceInfo

Description of PCI vGPU device and its capabilities.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | The vGPU device name.  ***Since:*** vSphere API 7.0.3.0  | 
**device_vendor_id** | **int** | A well-known unique identifier for the device.  It concatenates the 16-bit PCI vendor id in lower bits followed by 16-bit PCI device id.  ***Since:*** vSphere API 7.0.3.0  | 
**max_fb_size_in_gib** | **int** | The maximum framebuffer size in gibibytes.  ***Since:*** vSphere API 7.0.3.0  | 
**time_sliced_capable** | **bool** | Indicate whether device is time-sliced capable.  ***Since:*** vSphere API 7.0.3.0  | 
**mig_capable** | **bool** | Indicate whether device is Multiple Instance GPU capable.  ***Since:*** vSphere API 7.0.3.0  | 
**compute_profile_capable** | **bool** | Indicate whether device is compute profile capable.  ***Since:*** vSphere API 7.0.3.0  | 
**quadro_profile_capable** | **bool** | Indicate whether device is quadro profile capable.  ***Since:*** vSphere API 7.0.3.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_vgpu_device_info import VirtualMachineVgpuDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVgpuDeviceInfo from a JSON string
virtual_machine_vgpu_device_info_instance = VirtualMachineVgpuDeviceInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVgpuDeviceInfo.to_json()

# convert the object into a dict
virtual_machine_vgpu_device_info_dict = virtual_machine_vgpu_device_info_instance.to_dict()
# create an instance of VirtualMachineVgpuDeviceInfo from a dict
virtual_machine_vgpu_device_info_form_dict = virtual_machine_vgpu_device_info.from_dict(virtual_machine_vgpu_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


