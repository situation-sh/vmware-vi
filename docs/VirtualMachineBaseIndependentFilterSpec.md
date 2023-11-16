# VirtualMachineBaseIndependentFilterSpec

The BaseIndependentFilterSpec is base class for two different types of independent filter specs *VirtualMachineIndependentFilterSpec* and *VirtualMachineEmptyIndependentFilterSpec* which are used to specify independent filters to be attached/removed on VMs virtual disk.  ***Since:*** vSphere API 7.0.2.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_base_independent_filter_spec import VirtualMachineBaseIndependentFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineBaseIndependentFilterSpec from a JSON string
virtual_machine_base_independent_filter_spec_instance = VirtualMachineBaseIndependentFilterSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineBaseIndependentFilterSpec.to_json()

# convert the object into a dict
virtual_machine_base_independent_filter_spec_dict = virtual_machine_base_independent_filter_spec_instance.to_dict()
# create an instance of VirtualMachineBaseIndependentFilterSpec from a dict
virtual_machine_base_independent_filter_spec_form_dict = virtual_machine_base_independent_filter_spec.from_dict(virtual_machine_base_independent_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


