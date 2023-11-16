# FileInfo

This data object type contains rudimentary information about a file in a datastore.  The information here is not meant to cover all information in traditional file systems, but rather to provide sufficient information for files that are associated with virtual machines. Derived types describe the known file types for a datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path relative to the folder path in the search results.  | 
**friendly_name** | **str** | User friendly name.  ***Since:*** vSphere API 6.5  | [optional] 
**file_size** | **int** | The size of the file in bytes.  | [optional] 
**modification** | **datetime** | The last date and time the file was modified.  | [optional] 
**owner** | **str** | The user name of the owner of the file.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.file_info import FileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileInfo from a JSON string
file_info_instance = FileInfo.from_json(json)
# print the JSON string representation of the object
print FileInfo.to_json()

# convert the object into a dict
file_info_dict = file_info_instance.to_dict()
# create an instance of FileInfo from a dict
file_info_form_dict = file_info.from_dict(file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


