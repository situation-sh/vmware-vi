# FileTooLarge

This fault is thrown when an operation fails because the file is larger than the maximum file size supported by the datastore.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | **str** | The name of the datastore that does not support the file&#39;s size.  ***Since:*** VI API 2.5  | 
**file_size** | **int** | The size (in bytes) of the file.  ***Since:*** VI API 2.5  | 
**max_file_size** | **int** | The max file size (in bytes) supported on the datastore.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.file_too_large import FileTooLarge

# TODO update the JSON string below
json = "{}"
# create an instance of FileTooLarge from a JSON string
file_too_large_instance = FileTooLarge.from_json(json)
# print the JSON string representation of the object
print FileTooLarge.to_json()

# convert the object into a dict
file_too_large_dict = file_too_large_instance.to_dict()
# create an instance of FileTooLarge from a dict
file_too_large_form_dict = file_too_large.from_dict(file_too_large_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


