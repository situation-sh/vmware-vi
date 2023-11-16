# LookupVmOverheadMemoryRequestType

The parameters of *OverheadMemoryManager.LookupVmOverheadMemory*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.lookup_vm_overhead_memory_request_type import LookupVmOverheadMemoryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of LookupVmOverheadMemoryRequestType from a JSON string
lookup_vm_overhead_memory_request_type_instance = LookupVmOverheadMemoryRequestType.from_json(json)
# print the JSON string representation of the object
print LookupVmOverheadMemoryRequestType.to_json()

# convert the object into a dict
lookup_vm_overhead_memory_request_type_dict = lookup_vm_overhead_memory_request_type_instance.to_dict()
# create an instance of LookupVmOverheadMemoryRequestType from a dict
lookup_vm_overhead_memory_request_type_form_dict = lookup_vm_overhead_memory_request_type.from_dict(lookup_vm_overhead_memory_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


