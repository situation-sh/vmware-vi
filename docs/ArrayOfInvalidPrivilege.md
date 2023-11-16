# ArrayOfInvalidPrivilege

A boxed array of *InvalidPrivilege*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidPrivilege]**](InvalidPrivilege.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_privilege import ArrayOfInvalidPrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidPrivilege from a JSON string
array_of_invalid_privilege_instance = ArrayOfInvalidPrivilege.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidPrivilege.to_json()

# convert the object into a dict
array_of_invalid_privilege_dict = array_of_invalid_privilege_instance.to_dict()
# create an instance of ArrayOfInvalidPrivilege from a dict
array_of_invalid_privilege_form_dict = array_of_invalid_privilege.from_dict(array_of_invalid_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


