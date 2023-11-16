# GuestFileAttributes

Different attributes for a guest file. - Check *GuestPosixFileAttributes*   for Posix guest files. - Check *GuestWindowsFileAttributes*   for Windows guest files.    ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modification_time** | **datetime** | The date and time the file was last modified.  If this property is not specified when passing a *GuestFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest*, the default value will be the time when the file is created inside the guest.  ***Since:*** vSphere API 5.0  | [optional] 
**access_time** | **datetime** | The date and time the file was last accessed.  If this property is not specified when passing a *GuestFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest*, the default value will be the time when the file is created inside the guest.  ***Since:*** vSphere API 5.0  | [optional] 
**symlink_target** | **str** | The target for the file if it&#39;s a symbolic link.  This is currently only set for Linux guest operating systems, but may be supported in the future on Windows guest operating systems that support symbolic links. This property gives information about files when returned from *GuestFileManager.ListFilesInGuest* or *GuestFileManager.InitiateFileTransferFromGuest* as part of a *GuestFileAttributes* object. This property will be ignored when passing a *GuestFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest* or *GuestFileManager.ChangeFileAttributesInGuest*. If the file is a symbolic link, then the attributes of the target are returned, not those of the symbolic link.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_file_attributes import GuestFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GuestFileAttributes from a JSON string
guest_file_attributes_instance = GuestFileAttributes.from_json(json)
# print the JSON string representation of the object
print GuestFileAttributes.to_json()

# convert the object into a dict
guest_file_attributes_dict = guest_file_attributes_instance.to_dict()
# create an instance of GuestFileAttributes from a dict
guest_file_attributes_form_dict = guest_file_attributes.from_dict(guest_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


