# ArrayOfNoPermission

A boxed array of *NoPermission*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoPermission]**](NoPermission.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_permission import ArrayOfNoPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoPermission from a JSON string
array_of_no_permission_instance = ArrayOfNoPermission.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoPermission.to_json()

# convert the object into a dict
array_of_no_permission_dict = array_of_no_permission_instance.to_dict()
# create an instance of ArrayOfNoPermission from a dict
array_of_no_permission_form_dict = array_of_no_permission.from_dict(array_of_no_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


