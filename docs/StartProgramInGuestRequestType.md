# StartProgramInGuestRequestType

The parameters of *GuestProcessManager.StartProgramInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**spec** | [**GuestProgramSpec**](GuestProgramSpec.md) |  | 

## Example

```python
from vmware_vi.models.start_program_in_guest_request_type import StartProgramInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of StartProgramInGuestRequestType from a JSON string
start_program_in_guest_request_type_instance = StartProgramInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print StartProgramInGuestRequestType.to_json()

# convert the object into a dict
start_program_in_guest_request_type_dict = start_program_in_guest_request_type_instance.to_dict()
# create an instance of StartProgramInGuestRequestType from a dict
start_program_in_guest_request_type_form_dict = start_program_in_guest_request_type.from_dict(start_program_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


