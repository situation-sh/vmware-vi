# CannotCreateFile

A CannotCreateFile exception is thrown if a file create operation fails.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_create_file import CannotCreateFile

# TODO update the JSON string below
json = "{}"
# create an instance of CannotCreateFile from a JSON string
cannot_create_file_instance = CannotCreateFile.from_json(json)
# print the JSON string representation of the object
print CannotCreateFile.to_json()

# convert the object into a dict
cannot_create_file_dict = cannot_create_file_instance.to_dict()
# create an instance of CannotCreateFile from a dict
cannot_create_file_form_dict = cannot_create_file.from_dict(cannot_create_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


