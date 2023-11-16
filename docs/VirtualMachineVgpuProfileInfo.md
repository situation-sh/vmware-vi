# VirtualMachineVgpuProfileInfo

Description of PCI vGPU profile and its attributes.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_name** | **str** | The vGPU profile name.  ***Since:*** vSphere API 7.0.3.0  | 
**device_vendor_id** | **int** | A well-known unique identifier for the device that supports this profile.  It concatenates the 16-bit PCI vendor id in lower bits followed by 16-bit PCI device id.  ***Since:*** vSphere API 7.0.3.0  | 
**fb_size_in_gib** | **int** | The profile framebuffer size in gibibytes.  ***Since:*** vSphere API 7.0.3.0  | 
**profile_sharing** | **str** | Indicate how this profile is shared within device.  ***Since:*** vSphere API 7.0.3.0  | 
**profile_class** | **str** | Indicate class for this profile.  ***Since:*** vSphere API 7.0.3.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_vgpu_profile_info import VirtualMachineVgpuProfileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVgpuProfileInfo from a JSON string
virtual_machine_vgpu_profile_info_instance = VirtualMachineVgpuProfileInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVgpuProfileInfo.to_json()

# convert the object into a dict
virtual_machine_vgpu_profile_info_dict = virtual_machine_vgpu_profile_info_instance.to_dict()
# create an instance of VirtualMachineVgpuProfileInfo from a dict
virtual_machine_vgpu_profile_info_form_dict = virtual_machine_vgpu_profile_info.from_dict(virtual_machine_vgpu_profile_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


