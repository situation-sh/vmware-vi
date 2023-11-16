# DeleteDirectoryInGuestRequestType

The parameters of *GuestFileManager.DeleteDirectoryInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**directory_path** | **str** | The complete path to the directory to be deleted.  | 
**recursive** | **bool** | If true, all subdirectories are also deleted. If false, the directory must be empty for the operation to succeed.  | 

## Example

```python
from vmware_vi.models.delete_directory_in_guest_request_type import DeleteDirectoryInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDirectoryInGuestRequestType from a JSON string
delete_directory_in_guest_request_type_instance = DeleteDirectoryInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteDirectoryInGuestRequestType.to_json()

# convert the object into a dict
delete_directory_in_guest_request_type_dict = delete_directory_in_guest_request_type_instance.to_dict()
# create an instance of DeleteDirectoryInGuestRequestType from a dict
delete_directory_in_guest_request_type_form_dict = delete_directory_in_guest_request_type.from_dict(delete_directory_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


