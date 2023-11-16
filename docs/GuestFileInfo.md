# GuestFileInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The complete path to the file  ***Since:*** vSphere API 5.0  | 
**type** | **str** | The file type, one of *GuestFileType_enum*  ***Since:*** vSphere API 5.0  | 
**size** | **int** | The file size in bytes  ***Since:*** vSphere API 5.0  | 
**attributes** | [**GuestFileAttributes**](GuestFileAttributes.md) |  | 

## Example

```python
from vmware_vi.models.guest_file_info import GuestFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestFileInfo from a JSON string
guest_file_info_instance = GuestFileInfo.from_json(json)
# print the JSON string representation of the object
print GuestFileInfo.to_json()

# convert the object into a dict
guest_file_info_dict = guest_file_info_instance.to_dict()
# create an instance of GuestFileInfo from a dict
guest_file_info_form_dict = guest_file_info.from_dict(guest_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


