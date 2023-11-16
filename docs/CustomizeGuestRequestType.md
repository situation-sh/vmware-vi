# CustomizeGuestRequestType

The parameters of *VirtualMachineGuestCustomizationManager.CustomizeGuest_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**spec** | [**CustomizationSpec**](CustomizationSpec.md) |  | 
**config_params** | [**List[OptionValue]**](OptionValue.md) | addtional key/value pair list to support third party customization.  | [optional] 

## Example

```python
from vmware_vi.models.customize_guest_request_type import CustomizeGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeGuestRequestType from a JSON string
customize_guest_request_type_instance = CustomizeGuestRequestType.from_json(json)
# print the JSON string representation of the object
print CustomizeGuestRequestType.to_json()

# convert the object into a dict
customize_guest_request_type_dict = customize_guest_request_type_instance.to_dict()
# create an instance of CustomizeGuestRequestType from a dict
customize_guest_request_type_form_dict = customize_guest_request_type.from_dict(customize_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


