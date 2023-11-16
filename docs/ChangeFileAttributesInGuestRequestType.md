# ChangeFileAttributesInGuestRequestType

The parameters of *GuestFileManager.ChangeFileAttributesInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**guest_file_path** | **str** | The complete path to the file to be copied in the guest. If the file points to an symbolic link, then the attributes of the target file are changed.  | 
**file_attributes** | [**GuestFileAttributes**](GuestFileAttributes.md) |  | 

## Example

```python
from vmware_vi.models.change_file_attributes_in_guest_request_type import ChangeFileAttributesInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeFileAttributesInGuestRequestType from a JSON string
change_file_attributes_in_guest_request_type_instance = ChangeFileAttributesInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print ChangeFileAttributesInGuestRequestType.to_json()

# convert the object into a dict
change_file_attributes_in_guest_request_type_dict = change_file_attributes_in_guest_request_type_instance.to_dict()
# create an instance of ChangeFileAttributesInGuestRequestType from a dict
change_file_attributes_in_guest_request_type_form_dict = change_file_attributes_in_guest_request_type.from_dict(change_file_attributes_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


