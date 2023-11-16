# NotAFile

This fault is thrown when an operation fails because the specified object is not a file.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.not_a_file import NotAFile

# TODO update the JSON string below
json = "{}"
# create an instance of NotAFile from a JSON string
not_a_file_instance = NotAFile.from_json(json)
# print the JSON string representation of the object
print NotAFile.to_json()

# convert the object into a dict
not_a_file_dict = not_a_file_instance.to_dict()
# create an instance of NotAFile from a dict
not_a_file_form_dict = not_a_file.from_dict(not_a_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


