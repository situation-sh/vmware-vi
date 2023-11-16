# InsufficientHostCapacityFault

The host does not have enough capacity for running the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.insufficient_host_capacity_fault import InsufficientHostCapacityFault

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientHostCapacityFault from a JSON string
insufficient_host_capacity_fault_instance = InsufficientHostCapacityFault.from_json(json)
# print the JSON string representation of the object
print InsufficientHostCapacityFault.to_json()

# convert the object into a dict
insufficient_host_capacity_fault_dict = insufficient_host_capacity_fault_instance.to_dict()
# create an instance of InsufficientHostCapacityFault from a dict
insufficient_host_capacity_fault_form_dict = insufficient_host_capacity_fault.from_dict(insufficient_host_capacity_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


