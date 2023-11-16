# VirtualMachineCdromInfo

CdromInfo class contains information about a physical CD-ROM drive on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the physical device.  This is set only by the server.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_cdrom_info import VirtualMachineCdromInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineCdromInfo from a JSON string
virtual_machine_cdrom_info_instance = VirtualMachineCdromInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineCdromInfo.to_json()

# convert the object into a dict
virtual_machine_cdrom_info_dict = virtual_machine_cdrom_info_instance.to_dict()
# create an instance of VirtualMachineCdromInfo from a dict
virtual_machine_cdrom_info_form_dict = virtual_machine_cdrom_info.from_dict(virtual_machine_cdrom_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


