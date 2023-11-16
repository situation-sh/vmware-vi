# VirtualMachineEmptyProfileSpec

Specifies an empty Storage Policy for a Virtual Machine Home or a Virtual Disk object.  The object is left without any profile association, and hence has no explicit policy driven requirements. This implies that object's policy driven SLAs are always met trivially.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_empty_profile_spec import VirtualMachineEmptyProfileSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineEmptyProfileSpec from a JSON string
virtual_machine_empty_profile_spec_instance = VirtualMachineEmptyProfileSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineEmptyProfileSpec.to_json()

# convert the object into a dict
virtual_machine_empty_profile_spec_dict = virtual_machine_empty_profile_spec_instance.to_dict()
# create an instance of VirtualMachineEmptyProfileSpec from a dict
virtual_machine_empty_profile_spec_form_dict = virtual_machine_empty_profile_spec.from_dict(virtual_machine_empty_profile_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


