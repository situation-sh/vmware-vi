# ArrayOfNetworkCopyFault

A boxed array of *NetworkCopyFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetworkCopyFault]**](NetworkCopyFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_network_copy_fault import ArrayOfNetworkCopyFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetworkCopyFault from a JSON string
array_of_network_copy_fault_instance = ArrayOfNetworkCopyFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetworkCopyFault.to_json()

# convert the object into a dict
array_of_network_copy_fault_dict = array_of_network_copy_fault_instance.to_dict()
# create an instance of ArrayOfNetworkCopyFault from a dict
array_of_network_copy_fault_form_dict = array_of_network_copy_fault.from_dict(array_of_network_copy_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


