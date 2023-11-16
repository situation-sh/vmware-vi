# HostNotConnected

A HostNotConnected fault is thrown if a method needs to communicate with a host that has been disconnected in VirtualCenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_not_connected import HostNotConnected

# TODO update the JSON string below
json = "{}"
# create an instance of HostNotConnected from a JSON string
host_not_connected_instance = HostNotConnected.from_json(json)
# print the JSON string representation of the object
print HostNotConnected.to_json()

# convert the object into a dict
host_not_connected_dict = host_not_connected_instance.to_dict()
# create an instance of HostNotConnected from a dict
host_not_connected_form_dict = host_not_connected.from_dict(host_not_connected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


