# HostFileAccess

This data object type contains a single access control entry for a file permissions list. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**who** | **str** | User or group to which the access applies.  | 
**what** | **str** | Rights given to the user or group.  | 

## Example

```python
from vmware_vi.models.host_file_access import HostFileAccess

# TODO update the JSON string below
json = "{}"
# create an instance of HostFileAccess from a JSON string
host_file_access_instance = HostFileAccess.from_json(json)
# print the JSON string representation of the object
print HostFileAccess.to_json()

# convert the object into a dict
host_file_access_dict = host_file_access_instance.to_dict()
# create an instance of HostFileAccess from a dict
host_file_access_form_dict = host_file_access.from_dict(host_file_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


