# NotADirectory

This fault is thrown when an operation fails because the specified object is not a directory.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.not_a_directory import NotADirectory

# TODO update the JSON string below
json = "{}"
# create an instance of NotADirectory from a JSON string
not_a_directory_instance = NotADirectory.from_json(json)
# print the JSON string representation of the object
print NotADirectory.to_json()

# convert the object into a dict
not_a_directory_dict = not_a_directory_instance.to_dict()
# create an instance of NotADirectory from a dict
not_a_directory_form_dict = not_a_directory.from_dict(not_a_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


