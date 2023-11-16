# FileNameTooLong

This fault is thrown when an operation fails because the name of the specified file is too long.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.file_name_too_long import FileNameTooLong

# TODO update the JSON string below
json = "{}"
# create an instance of FileNameTooLong from a JSON string
file_name_too_long_instance = FileNameTooLong.from_json(json)
# print the JSON string representation of the object
print FileNameTooLong.to_json()

# convert the object into a dict
file_name_too_long_dict = file_name_too_long_instance.to_dict()
# create an instance of FileNameTooLong from a dict
file_name_too_long_form_dict = file_name_too_long.from_dict(file_name_too_long_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


