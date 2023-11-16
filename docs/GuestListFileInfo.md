# GuestListFileInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[GuestFileInfo]**](GuestFileInfo.md) | A list of *GuestFileInfo* data objects containing information for all the matching files.  ***Since:*** vSphere API 5.0  | [optional] 
**remaining** | **int** | The number of files left to be returned.  If non-zero, then the next set of files can be returned by calling ListFiles again with the index set to the number of results already returned.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.guest_list_file_info import GuestListFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestListFileInfo from a JSON string
guest_list_file_info_instance = GuestListFileInfo.from_json(json)
# print the JSON string representation of the object
print GuestListFileInfo.to_json()

# convert the object into a dict
guest_list_file_info_dict = guest_list_file_info_instance.to_dict()
# create an instance of GuestListFileInfo from a dict
guest_list_file_info_form_dict = guest_list_file_info.from_dict(guest_list_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


