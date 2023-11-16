# VirtualMachineDefaultProfileSpec

Used to indicate that the Default Storage Policy of the target datastore be used for a Virtual Machine Home or a Virtual Disk object.  Neither the association nor the policy data is persisted in Virtual Machine configuration. This data is managed by an extension of Virtual Center (Storage Policy Based Management).  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_default_profile_spec import VirtualMachineDefaultProfileSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDefaultProfileSpec from a JSON string
virtual_machine_default_profile_spec_instance = VirtualMachineDefaultProfileSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDefaultProfileSpec.to_json()

# convert the object into a dict
virtual_machine_default_profile_spec_dict = virtual_machine_default_profile_spec_instance.to_dict()
# create an instance of VirtualMachineDefaultProfileSpec from a dict
virtual_machine_default_profile_spec_form_dict = virtual_machine_default_profile_spec.from_dict(virtual_machine_default_profile_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


