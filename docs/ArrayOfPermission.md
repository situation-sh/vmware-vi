# ArrayOfPermission

A boxed array of *Permission*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Permission]**](Permission.md) |  | 

## Example

```python
from vmware_vi.models.array_of_permission import ArrayOfPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPermission from a JSON string
array_of_permission_instance = ArrayOfPermission.from_json(json)
# print the JSON string representation of the object
print ArrayOfPermission.to_json()

# convert the object into a dict
array_of_permission_dict = array_of_permission_instance.to_dict()
# create an instance of ArrayOfPermission from a dict
array_of_permission_form_dict = array_of_permission.from_dict(array_of_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


