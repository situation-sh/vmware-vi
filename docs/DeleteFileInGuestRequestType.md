# DeleteFileInGuestRequestType

The parameters of *GuestFileManager.DeleteFileInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**file_path** | **str** | The complete path to the file or symbolic link to be deleted.  | 

## Example

```python
from vmware_vi.models.delete_file_in_guest_request_type import DeleteFileInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFileInGuestRequestType from a JSON string
delete_file_in_guest_request_type_instance = DeleteFileInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteFileInGuestRequestType.to_json()

# convert the object into a dict
delete_file_in_guest_request_type_dict = delete_file_in_guest_request_type_instance.to_dict()
# create an instance of DeleteFileInGuestRequestType from a dict
delete_file_in_guest_request_type_form_dict = delete_file_in_guest_request_type.from_dict(delete_file_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


