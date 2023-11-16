# InitiateFileTransferToGuestRequestType

The parameters of *GuestFileManager.InitiateFileTransferToGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**guest_file_path** | **str** | The complete destination path in the guest to transfer the file from the client. It cannot be a path to a directory or a symbolic link.  | 
**file_attributes** | [**GuestFileAttributes**](GuestFileAttributes.md) |  | 
**file_size** | **int** | Size of the file to transfer to the guest in bytes.  | 
**overwrite** | **bool** | If set, the destination file is clobbered.  | 

## Example

```python
from vmware_vi.models.initiate_file_transfer_to_guest_request_type import InitiateFileTransferToGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateFileTransferToGuestRequestType from a JSON string
initiate_file_transfer_to_guest_request_type_instance = InitiateFileTransferToGuestRequestType.from_json(json)
# print the JSON string representation of the object
print InitiateFileTransferToGuestRequestType.to_json()

# convert the object into a dict
initiate_file_transfer_to_guest_request_type_dict = initiate_file_transfer_to_guest_request_type_instance.to_dict()
# create an instance of InitiateFileTransferToGuestRequestType from a dict
initiate_file_transfer_to_guest_request_type_form_dict = initiate_file_transfer_to_guest_request_type.from_dict(initiate_file_transfer_to_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


