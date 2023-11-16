# HostNotReachable

A HostNotReachable fault is thrown if the server was unable to communicate with the host 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_not_reachable import HostNotReachable

# TODO update the JSON string below
json = "{}"
# create an instance of HostNotReachable from a JSON string
host_not_reachable_instance = HostNotReachable.from_json(json)
# print the JSON string representation of the object
print HostNotReachable.to_json()

# convert the object into a dict
host_not_reachable_dict = host_not_reachable_instance.to_dict()
# create an instance of HostNotReachable from a dict
host_not_reachable_form_dict = host_not_reachable.from_dict(host_not_reachable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


