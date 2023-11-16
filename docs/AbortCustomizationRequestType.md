# AbortCustomizationRequestType

The parameters of *VirtualMachineGuestCustomizationManager.AbortCustomization_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.abort_customization_request_type import AbortCustomizationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AbortCustomizationRequestType from a JSON string
abort_customization_request_type_instance = AbortCustomizationRequestType.from_json(json)
# print the JSON string representation of the object
print AbortCustomizationRequestType.to_json()

# convert the object into a dict
abort_customization_request_type_dict = abort_customization_request_type_instance.to_dict()
# create an instance of AbortCustomizationRequestType from a dict
abort_customization_request_type_form_dict = abort_customization_request_type.from_dict(abort_customization_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


