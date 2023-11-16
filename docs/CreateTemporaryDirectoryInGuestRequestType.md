# CreateTemporaryDirectoryInGuestRequestType

The parameters of *GuestFileManager.CreateTemporaryDirectoryInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**prefix** | **str** | The prefix to be given to the new temporary directory.  | 
**suffix** | **str** | The suffix to be given to the new temporary directory.  | 
**directory_path** | **str** | The complete path to the directory in which to create the new directory. If unset or an empty string, a guest-specific location will be used.  | [optional] 

## Example

```python
from vmware_vi.models.create_temporary_directory_in_guest_request_type import CreateTemporaryDirectoryInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemporaryDirectoryInGuestRequestType from a JSON string
create_temporary_directory_in_guest_request_type_instance = CreateTemporaryDirectoryInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print CreateTemporaryDirectoryInGuestRequestType.to_json()

# convert the object into a dict
create_temporary_directory_in_guest_request_type_dict = create_temporary_directory_in_guest_request_type_instance.to_dict()
# create an instance of CreateTemporaryDirectoryInGuestRequestType from a dict
create_temporary_directory_in_guest_request_type_form_dict = create_temporary_directory_in_guest_request_type.from_dict(create_temporary_directory_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


