# ArrayOfHostConnectFault

A boxed array of *HostConnectFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConnectFault]**](HostConnectFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_connect_fault import ArrayOfHostConnectFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConnectFault from a JSON string
array_of_host_connect_fault_instance = ArrayOfHostConnectFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConnectFault.to_json()

# convert the object into a dict
array_of_host_connect_fault_dict = array_of_host_connect_fault_instance.to_dict()
# create an instance of ArrayOfHostConnectFault from a dict
array_of_host_connect_fault_form_dict = array_of_host_connect_fault.from_dict(array_of_host_connect_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


