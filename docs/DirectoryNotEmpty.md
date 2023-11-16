# DirectoryNotEmpty

This fault is thrown when an operation fails because the specified directory is not empty.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.directory_not_empty import DirectoryNotEmpty

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoryNotEmpty from a JSON string
directory_not_empty_instance = DirectoryNotEmpty.from_json(json)
# print the JSON string representation of the object
print DirectoryNotEmpty.to_json()

# convert the object into a dict
directory_not_empty_dict = directory_not_empty_instance.to_dict()
# create an instance of DirectoryNotEmpty from a dict
directory_not_empty_form_dict = directory_not_empty.from_dict(directory_not_empty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


