# ArrayOfFileLocked

A boxed array of *FileLocked*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FileLocked]**](FileLocked.md) |  | 

## Example

```python
from vmware_vi.models.array_of_file_locked import ArrayOfFileLocked

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFileLocked from a JSON string
array_of_file_locked_instance = ArrayOfFileLocked.from_json(json)
# print the JSON string representation of the object
print ArrayOfFileLocked.to_json()

# convert the object into a dict
array_of_file_locked_dict = array_of_file_locked_instance.to_dict()
# create an instance of ArrayOfFileLocked from a dict
array_of_file_locked_form_dict = array_of_file_locked.from_dict(array_of_file_locked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


