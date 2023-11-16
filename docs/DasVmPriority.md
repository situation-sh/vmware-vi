# DasVmPriority

A boxed *DasVmPriority_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**DasVmPriorityEnum**](DasVmPriorityEnum.md) |  | 

## Example

```python
from vmware_vi.models.das_vm_priority import DasVmPriority

# TODO update the JSON string below
json = "{}"
# create an instance of DasVmPriority from a JSON string
das_vm_priority_instance = DasVmPriority.from_json(json)
# print the JSON string representation of the object
print DasVmPriority.to_json()

# convert the object into a dict
das_vm_priority_dict = das_vm_priority_instance.to_dict()
# create an instance of DasVmPriority from a dict
das_vm_priority_form_dict = das_vm_priority.from_dict(das_vm_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


