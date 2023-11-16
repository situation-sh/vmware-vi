# VirtualMachineEmptyIndependentFilterSpec

The EmptyIndependentFilterSpec data object is used to specify empty independent filter spec.  This obejct is passed during provisioning workflows to remove all attached independent filters.  ***Since:*** vSphere API 7.0.2.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_empty_independent_filter_spec import VirtualMachineEmptyIndependentFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineEmptyIndependentFilterSpec from a JSON string
virtual_machine_empty_independent_filter_spec_instance = VirtualMachineEmptyIndependentFilterSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineEmptyIndependentFilterSpec.to_json()

# convert the object into a dict
virtual_machine_empty_independent_filter_spec_dict = virtual_machine_empty_independent_filter_spec_instance.to_dict()
# create an instance of VirtualMachineEmptyIndependentFilterSpec from a dict
virtual_machine_empty_independent_filter_spec_form_dict = virtual_machine_empty_independent_filter_spec.from_dict(virtual_machine_empty_independent_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


