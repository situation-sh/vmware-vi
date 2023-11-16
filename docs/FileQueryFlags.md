# FileQueryFlags

The FileInfo.Details data object type is a set of flags for a search request.  This search request specifies which details to return for each matching file. This data object type is here to ensure that there is one flag corresponding to each FileInfo property other than the path name, which a search always returns. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_type** | **bool** | The flag to indicate whether or not the files that match this query specification are returned along with file type information.  This field must be set to return specific details about the file type.  | 
**file_size** | **bool** | The flag to indicate whether or not the size of the file is returned.  | 
**modification** | **bool** | The flag to indicate whether or not to return the date and time the file was last modified.  | 
**file_owner** | **bool** | The flag to indicate whether or not to return the file owner.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.file_query_flags import FileQueryFlags

# TODO update the JSON string below
json = "{}"
# create an instance of FileQueryFlags from a JSON string
file_query_flags_instance = FileQueryFlags.from_json(json)
# print the JSON string representation of the object
print FileQueryFlags.to_json()

# convert the object into a dict
file_query_flags_dict = file_query_flags_instance.to_dict()
# create an instance of FileQueryFlags from a dict
file_query_flags_form_dict = file_query_flags.from_dict(file_query_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


