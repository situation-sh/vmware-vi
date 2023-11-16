# FileLocked

Thrown if an attempt is made to lock a file that is already in use. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.file_locked import FileLocked

# TODO update the JSON string below
json = "{}"
# create an instance of FileLocked from a JSON string
file_locked_instance = FileLocked.from_json(json)
# print the JSON string representation of the object
print FileLocked.to_json()

# convert the object into a dict
file_locked_dict = file_locked_instance.to_dict()
# create an instance of FileLocked from a dict
file_locked_form_dict = file_locked.from_dict(file_locked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


