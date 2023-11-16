# TerminateProcessInGuestRequestType

The parameters of *GuestProcessManager.TerminateProcessInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**pid** | **int** | Process ID of the process to be terminated  | 

## Example

```python
from vmware_vi.models.terminate_process_in_guest_request_type import TerminateProcessInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateProcessInGuestRequestType from a JSON string
terminate_process_in_guest_request_type_instance = TerminateProcessInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print TerminateProcessInGuestRequestType.to_json()

# convert the object into a dict
terminate_process_in_guest_request_type_dict = terminate_process_in_guest_request_type_instance.to_dict()
# create an instance of TerminateProcessInGuestRequestType from a dict
terminate_process_in_guest_request_type_form_dict = terminate_process_in_guest_request_type.from_dict(terminate_process_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


