# VirtualMachineVideoCard

The VirtualVideoCard data object type represents a video card in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_ram_size_in_kb** | **int** | The size of the framebuffer for a virtual machine.  | [optional] 
**num_displays** | **int** | Indicates the number of supported monitors.  The number of displays X the maximum resolution of each display is bounded by the video RAM size of the virtual video card. This property can only be updated when the virtual machine is powered off.  ***Since:*** vSphere API 4.0  | [optional] 
**use_auto_detect** | **bool** | Flag to indicate whether the display settings of the host on which the virtual machine is running should be used to automatically determine the display settings of the virtual machine&#39;s video card.  This setting takes effect at virtual machine power-on time. If this value is set to TRUE, numDisplays will be ignored.  ***Since:*** vSphere API 4.0  | [optional] 
**enable3_d_support** | **bool** | Flag to indicate whether the virtual video card supports 3D functions.  This property can only be updated when the virtual machine is powered off.  ***Since:*** vSphere API 4.0  | [optional] 
**use3d_renderer** | **str** | Indicate how the virtual video device renders 3D graphics.  The virtual video device can use hardware acceleration and software rendering. By default, VMware products determine whether or not to use hardware acceleration based on the availability of physical graphics devices. Certain workloads can benefit from explicitly specifying if hardware acceleration is required. For example, 3D intensive workloads may indicate to run on systems with graphics hardware.  There are three settings.  (automatic) - The virtual device chooses how to render 3D graphics (default). (software) - The virtual device will use software rendering and will not attempt to use hardware acceleration. (hardware) - The virtual device will use hardware acceleration and will not activate without it.  ***Since:*** vSphere API 5.1  | [optional] 
**graphics_memory_size_in_kb** | **int** | The size of graphics memory.  If 3d support is enabled this setting gives the amount of guest memory used for graphics resources. This property can only be updated when the virtual machine is powered off.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_video_card import VirtualMachineVideoCard

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVideoCard from a JSON string
virtual_machine_video_card_instance = VirtualMachineVideoCard.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVideoCard.to_json()

# convert the object into a dict
virtual_machine_video_card_dict = virtual_machine_video_card_instance.to_dict()
# create an instance of VirtualMachineVideoCard from a dict
virtual_machine_video_card_form_dict = virtual_machine_video_card.from_dict(virtual_machine_video_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


