# ArrayOfMountError

A boxed array of *MountError*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MountError]**](MountError.md) |  | 

## Example

```python
from vmware_vi.models.array_of_mount_error import ArrayOfMountError

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMountError from a JSON string
array_of_mount_error_instance = ArrayOfMountError.from_json(json)
# print the JSON string representation of the object
print ArrayOfMountError.to_json()

# convert the object into a dict
array_of_mount_error_dict = array_of_mount_error_instance.to_dict()
# create an instance of ArrayOfMountError from a dict
array_of_mount_error_form_dict = array_of_mount_error.from_dict(array_of_mount_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


