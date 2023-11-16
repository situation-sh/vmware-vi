# ArrayOfDasVmPriority

A boxed array of *DasVmPriority_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DasVmPriorityEnum]**](DasVmPriorityEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_das_vm_priority import ArrayOfDasVmPriority

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDasVmPriority from a JSON string
array_of_das_vm_priority_instance = ArrayOfDasVmPriority.from_json(json)
# print the JSON string representation of the object
print ArrayOfDasVmPriority.to_json()

# convert the object into a dict
array_of_das_vm_priority_dict = array_of_das_vm_priority_instance.to_dict()
# create an instance of ArrayOfDasVmPriority from a dict
array_of_das_vm_priority_form_dict = array_of_das_vm_priority.from_dict(array_of_das_vm_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


