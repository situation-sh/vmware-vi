# InvalidResourcePoolStructureFault

This fault is thrown when an operation will cause the structure of a resource pool hiearchy to exceed its limit.  The limits are typically imposed by the total number of nodes, maximum fan-out, and total depth of the hierarchy. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_resource_pool_structure_fault import InvalidResourcePoolStructureFault

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidResourcePoolStructureFault from a JSON string
invalid_resource_pool_structure_fault_instance = InvalidResourcePoolStructureFault.from_json(json)
# print the JSON string representation of the object
print InvalidResourcePoolStructureFault.to_json()

# convert the object into a dict
invalid_resource_pool_structure_fault_dict = invalid_resource_pool_structure_fault_instance.to_dict()
# create an instance of InvalidResourcePoolStructureFault from a dict
invalid_resource_pool_structure_fault_form_dict = invalid_resource_pool_structure_fault.from_dict(invalid_resource_pool_structure_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


