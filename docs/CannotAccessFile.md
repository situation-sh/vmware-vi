# CannotAccessFile

This fault is thrown when an operation fails because of insufficient permissions to access a file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_access_file import CannotAccessFile

# TODO update the JSON string below
json = "{}"
# create an instance of CannotAccessFile from a JSON string
cannot_access_file_instance = CannotAccessFile.from_json(json)
# print the JSON string representation of the object
print CannotAccessFile.to_json()

# convert the object into a dict
cannot_access_file_dict = cannot_access_file_instance.to_dict()
# create an instance of CannotAccessFile from a dict
cannot_access_file_form_dict = cannot_access_file.from_dict(cannot_access_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


