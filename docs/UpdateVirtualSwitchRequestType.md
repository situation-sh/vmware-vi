# UpdateVirtualSwitchRequestType

The parameters of *HostNetworkSystem.UpdateVirtualSwitch*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vswitch_name** | **str** |  | 
**spec** | [**HostVirtualSwitchSpec**](HostVirtualSwitchSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_virtual_switch_request_type import UpdateVirtualSwitchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVirtualSwitchRequestType from a JSON string
update_virtual_switch_request_type_instance = UpdateVirtualSwitchRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVirtualSwitchRequestType.to_json()

# convert the object into a dict
update_virtual_switch_request_type_dict = update_virtual_switch_request_type_instance.to_dict()
# create an instance of UpdateVirtualSwitchRequestType from a dict
update_virtual_switch_request_type_form_dict = update_virtual_switch_request_type.from_dict(update_virtual_switch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


