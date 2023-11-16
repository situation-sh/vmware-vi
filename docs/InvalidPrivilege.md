# InvalidPrivilege

A InvalidPrivilege fault is thrown when the privilege does not exist. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privilege** | **str** | The invalid privilege.  | 

## Example

```python
from vmware_vi.models.invalid_privilege import InvalidPrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPrivilege from a JSON string
invalid_privilege_instance = InvalidPrivilege.from_json(json)
# print the JSON string representation of the object
print InvalidPrivilege.to_json()

# convert the object into a dict
invalid_privilege_dict = invalid_privilege_instance.to_dict()
# create an instance of InvalidPrivilege from a dict
invalid_privilege_form_dict = invalid_privilege.from_dict(invalid_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


