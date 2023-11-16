# CannotDeleteFile

A CannotDeleteFile exception is thrown if a file-deletion operation fails. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_delete_file import CannotDeleteFile

# TODO update the JSON string below
json = "{}"
# create an instance of CannotDeleteFile from a JSON string
cannot_delete_file_instance = CannotDeleteFile.from_json(json)
# print the JSON string representation of the object
print CannotDeleteFile.to_json()

# convert the object into a dict
cannot_delete_file_dict = cannot_delete_file_instance.to_dict()
# create an instance of CannotDeleteFile from a dict
cannot_delete_file_form_dict = cannot_delete_file.from_dict(cannot_delete_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


