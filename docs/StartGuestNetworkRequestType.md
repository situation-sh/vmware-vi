# StartGuestNetworkRequestType

The parameters of *VirtualMachineGuestCustomizationManager.StartGuestNetwork_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.start_guest_network_request_type import StartGuestNetworkRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of StartGuestNetworkRequestType from a JSON string
start_guest_network_request_type_instance = StartGuestNetworkRequestType.from_json(json)
# print the JSON string representation of the object
print StartGuestNetworkRequestType.to_json()

# convert the object into a dict
start_guest_network_request_type_dict = start_guest_network_request_type_instance.to_dict()
# create an instance of StartGuestNetworkRequestType from a dict
start_guest_network_request_type_form_dict = start_guest_network_request_type.from_dict(start_guest_network_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


