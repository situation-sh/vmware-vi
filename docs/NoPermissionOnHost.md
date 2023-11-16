# NoPermissionOnHost

This indicates that the user account used to connect to the host does not have enough permissions to enable VirtualCenter to manage the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_permission_on_host import NoPermissionOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of NoPermissionOnHost from a JSON string
no_permission_on_host_instance = NoPermissionOnHost.from_json(json)
# print the JSON string representation of the object
print NoPermissionOnHost.to_json()

# convert the object into a dict
no_permission_on_host_dict = no_permission_on_host_instance.to_dict()
# create an instance of NoPermissionOnHost from a dict
no_permission_on_host_form_dict = no_permission_on_host.from_dict(no_permission_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


