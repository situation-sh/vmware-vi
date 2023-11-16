# FileAlreadyExists

This fault is thrown when an operation attempts to create a file using the name of an existing file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.file_already_exists import FileAlreadyExists

# TODO update the JSON string below
json = "{}"
# create an instance of FileAlreadyExists from a JSON string
file_already_exists_instance = FileAlreadyExists.from_json(json)
# print the JSON string representation of the object
print FileAlreadyExists.to_json()

# convert the object into a dict
file_already_exists_dict = file_already_exists_instance.to_dict()
# create an instance of FileAlreadyExists from a dict
file_already_exists_form_dict = file_already_exists.from_dict(file_already_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


