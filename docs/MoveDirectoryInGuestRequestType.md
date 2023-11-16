# MoveDirectoryInGuestRequestType

The parameters of *GuestFileManager.MoveDirectoryInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**src_directory_path** | **str** | The complete path to the directory to be moved.  | 
**dst_directory_path** | **str** | The complete path to the where the directory is moved or its new name. It cannot be a path to an existing directory or an existing file.  | 

## Example

```python
from vmware_vi.models.move_directory_in_guest_request_type import MoveDirectoryInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveDirectoryInGuestRequestType from a JSON string
move_directory_in_guest_request_type_instance = MoveDirectoryInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print MoveDirectoryInGuestRequestType.to_json()

# convert the object into a dict
move_directory_in_guest_request_type_dict = move_directory_in_guest_request_type_instance.to_dict()
# create an instance of MoveDirectoryInGuestRequestType from a dict
move_directory_in_guest_request_type_form_dict = move_directory_in_guest_request_type.from_dict(move_directory_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


