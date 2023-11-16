# MakeDirectoryInGuestRequestType

The parameters of *GuestFileManager.MakeDirectoryInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**directory_path** | **str** | The complete path to the directory to be created.  | 
**create_parent_directories** | **bool** | Whether any parent directories are to be created.  | 

## Example

```python
from vmware_vi.models.make_directory_in_guest_request_type import MakeDirectoryInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MakeDirectoryInGuestRequestType from a JSON string
make_directory_in_guest_request_type_instance = MakeDirectoryInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print MakeDirectoryInGuestRequestType.to_json()

# convert the object into a dict
make_directory_in_guest_request_type_dict = make_directory_in_guest_request_type_instance.to_dict()
# create an instance of MakeDirectoryInGuestRequestType from a dict
make_directory_in_guest_request_type_form_dict = make_directory_in_guest_request_type.from_dict(make_directory_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


