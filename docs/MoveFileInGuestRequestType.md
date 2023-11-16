# MoveFileInGuestRequestType

The parameters of *GuestFileManager.MoveFileInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**src_file_path** | **str** | The complete path to the original file or symbolic link to be moved.  | 
**dst_file_path** | **str** | The complete path to the where the file is renamed. It cannot be a path to an existing directory.  | 
**overwrite** | **bool** | If set, the destination file is clobbered.  | 

## Example

```python
from vmware_vi.models.move_file_in_guest_request_type import MoveFileInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFileInGuestRequestType from a JSON string
move_file_in_guest_request_type_instance = MoveFileInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print MoveFileInGuestRequestType.to_json()

# convert the object into a dict
move_file_in_guest_request_type_dict = move_file_in_guest_request_type_instance.to_dict()
# create an instance of MoveFileInGuestRequestType from a dict
move_file_in_guest_request_type_form_dict = move_file_in_guest_request_type.from_dict(move_file_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


