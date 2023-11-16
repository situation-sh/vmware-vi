# GuestPosixFileAttributes

Different attributes for Posix guest file.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **int** | The owner ID.  If this property is not specified when passing a *GuestPosixFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest*, the default value will be the owner Id of the user who invoked the file transfer operation.  ***Since:*** vSphere API 5.0  | [optional] 
**group_id** | **int** | The group ID.  If this property is not specified when passing a *GuestPosixFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest*, the default value will be the group Id of the user who invoked the file transfer operation.  ***Since:*** vSphere API 5.0  | [optional] 
**permissions** | **int** | The file permissions.  When creating a file with *GuestFileManager.InitiateFileTransferToGuest*, these are in chmod(2) format. When reporting on existing files, these are in stat(2) format. If this property is not specified when passing a *GuestPosixFileAttributes* object to *GuestFileManager.InitiateFileTransferToGuest*, the file will be created with 0644 permissions.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_posix_file_attributes import GuestPosixFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GuestPosixFileAttributes from a JSON string
guest_posix_file_attributes_instance = GuestPosixFileAttributes.from_json(json)
# print the JSON string representation of the object
print GuestPosixFileAttributes.to_json()

# convert the object into a dict
guest_posix_file_attributes_dict = guest_posix_file_attributes_instance.to_dict()
# create an instance of GuestPosixFileAttributes from a dict
guest_posix_file_attributes_form_dict = guest_posix_file_attributes.from_dict(guest_posix_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


