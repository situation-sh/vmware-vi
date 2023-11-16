# InitiateFileTransferFromGuestRequestType

The parameters of *GuestFileManager.InitiateFileTransferFromGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**guest_file_path** | **str** | The complete path to the file inside the guest that has to be transferred to the client. It cannot be a path to a directory or a symbolic link.  | 

## Example

```python
from vmware_vi.models.initiate_file_transfer_from_guest_request_type import InitiateFileTransferFromGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateFileTransferFromGuestRequestType from a JSON string
initiate_file_transfer_from_guest_request_type_instance = InitiateFileTransferFromGuestRequestType.from_json(json)
# print the JSON string representation of the object
print InitiateFileTransferFromGuestRequestType.to_json()

# convert the object into a dict
initiate_file_transfer_from_guest_request_type_dict = initiate_file_transfer_from_guest_request_type_instance.to_dict()
# create an instance of InitiateFileTransferFromGuestRequestType from a dict
initiate_file_transfer_from_guest_request_type_form_dict = initiate_file_transfer_from_guest_request_type.from_dict(initiate_file_transfer_from_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


