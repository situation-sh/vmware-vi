# VirtualMachineProfileSpec

The ProfileSpec data object is used to specify the Storage Policy to be associated with a Virtual Machine Home or a Virtual Disk.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_profile_spec import VirtualMachineProfileSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineProfileSpec from a JSON string
virtual_machine_profile_spec_instance = VirtualMachineProfileSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineProfileSpec.to_json()

# convert the object into a dict
virtual_machine_profile_spec_dict = virtual_machine_profile_spec_instance.to_dict()
# create an instance of VirtualMachineProfileSpec from a dict
virtual_machine_profile_spec_form_dict = virtual_machine_profile_spec.from_dict(virtual_machine_profile_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


