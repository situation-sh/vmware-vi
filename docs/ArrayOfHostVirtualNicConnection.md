# ArrayOfHostVirtualNicConnection

A boxed array of *HostVirtualNicConnection*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVirtualNicConnection]**](HostVirtualNicConnection.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_virtual_nic_connection import ArrayOfHostVirtualNicConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVirtualNicConnection from a JSON string
array_of_host_virtual_nic_connection_instance = ArrayOfHostVirtualNicConnection.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVirtualNicConnection.to_json()

# convert the object into a dict
array_of_host_virtual_nic_connection_dict = array_of_host_virtual_nic_connection_instance.to_dict()
# create an instance of ArrayOfHostVirtualNicConnection from a dict
array_of_host_virtual_nic_connection_form_dict = array_of_host_virtual_nic_connection.from_dict(array_of_host_virtual_nic_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


