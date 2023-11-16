# VirtualMachineGuestIntegrityInfo

This data object describes the guest integrity platform configuration of this virtual machine.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag to indicate whether guest integrity platform feature is enabled for this virtual machine.  Guest integrity adds capabilities in the virtual platform to detect attacks on the guest OS kernel  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_guest_integrity_info import VirtualMachineGuestIntegrityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineGuestIntegrityInfo from a JSON string
virtual_machine_guest_integrity_info_instance = VirtualMachineGuestIntegrityInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineGuestIntegrityInfo.to_json()

# convert the object into a dict
virtual_machine_guest_integrity_info_dict = virtual_machine_guest_integrity_info_instance.to_dict()
# create an instance of VirtualMachineGuestIntegrityInfo from a dict
virtual_machine_guest_integrity_info_form_dict = virtual_machine_guest_integrity_info.from_dict(virtual_machine_guest_integrity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


