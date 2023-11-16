# VirtualMachineSoundInfo

SoundInfo class contains information about a physical sound card on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_sound_info import VirtualMachineSoundInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSoundInfo from a JSON string
virtual_machine_sound_info_instance = VirtualMachineSoundInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSoundInfo.to_json()

# convert the object into a dict
virtual_machine_sound_info_dict = virtual_machine_sound_info_instance.to_dict()
# create an instance of VirtualMachineSoundInfo from a dict
virtual_machine_sound_info_form_dict = virtual_machine_sound_info.from_dict(virtual_machine_sound_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


