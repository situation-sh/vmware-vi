# HostAccountSpec

This data object type contains common parameters for local account creation.  The password and description properties are not supported for group accounts on POSIX hosts. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the specified account.  | 
**password** | **str** | The password for a user or group.  | [optional] 
**description** | **str** | The description of the specified account.  | [optional] 

## Example

```python
from vmware_vi.models.host_account_spec import HostAccountSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostAccountSpec from a JSON string
host_account_spec_instance = HostAccountSpec.from_json(json)
# print the JSON string representation of the object
print HostAccountSpec.to_json()

# convert the object into a dict
host_account_spec_dict = host_account_spec_instance.to_dict()
# create an instance of HostAccountSpec from a dict
host_account_spec_form_dict = host_account_spec.from_dict(host_account_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


