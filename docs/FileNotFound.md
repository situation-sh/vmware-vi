# FileNotFound

This fault is thrown when an operation fails because the specified file does not exist. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.file_not_found import FileNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of FileNotFound from a JSON string
file_not_found_instance = FileNotFound.from_json(json)
# print the JSON string representation of the object
print FileNotFound.to_json()

# convert the object into a dict
file_not_found_dict = file_not_found_instance.to_dict()
# create an instance of FileNotFound from a dict
file_not_found_form_dict = file_not_found.from_dict(file_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


