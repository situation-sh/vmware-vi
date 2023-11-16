# ListProcessesInGuestRequestType

The parameters of *GuestProcessManager.ListProcessesInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**pids** | **List[int]** | If set, only return information about the specified processes. Otherwise, information about all processes are returned. If a specified processes does not exist, nothing will be returned for that process.  | [optional] 

## Example

```python
from vmware_vi.models.list_processes_in_guest_request_type import ListProcessesInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListProcessesInGuestRequestType from a JSON string
list_processes_in_guest_request_type_instance = ListProcessesInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print ListProcessesInGuestRequestType.to_json()

# convert the object into a dict
list_processes_in_guest_request_type_dict = list_processes_in_guest_request_type_instance.to_dict()
# create an instance of ListProcessesInGuestRequestType from a dict
list_processes_in_guest_request_type_form_dict = list_processes_in_guest_request_type.from_dict(list_processes_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


