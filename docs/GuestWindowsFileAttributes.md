# GuestWindowsFileAttributes

Different attributes for a Windows guest file.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | The file is hidden.  If this property is not specified when passing a *GuestWindowsFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest*, the file will not be set as a hidden file.  ***Since:*** vSphere API 5.0  | [optional] 
**read_only** | **bool** | The file is read-only.  If this property is not specified when passing a *GuestWindowsFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest*, the file will not be set as a read-only file.  ***Since:*** vSphere API 5.0  | [optional] 
**create_time** | **datetime** | The date and time the file was created.  This property gives information about files when returned from *GuestFileManager.ListFilesInGuest* or *GuestFileManager.InitiateFileTransferFromGuest* as part of a *GuestWindowsFileAttributes* object. This property will be ignored when passing a *GuestWindowsFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest* or *GuestFileManager.ChangeFileAttributesInGuest*.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_windows_file_attributes import GuestWindowsFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GuestWindowsFileAttributes from a JSON string
guest_windows_file_attributes_instance = GuestWindowsFileAttributes.from_json(json)
# print the JSON string representation of the object
print GuestWindowsFileAttributes.to_json()

# convert the object into a dict
guest_windows_file_attributes_dict = guest_windows_file_attributes_instance.to_dict()
# create an instance of GuestWindowsFileAttributes from a dict
guest_windows_file_attributes_form_dict = guest_windows_file_attributes.from_dict(guest_windows_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


