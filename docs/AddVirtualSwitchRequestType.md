# AddVirtualSwitchRequestType

The parameters of *HostNetworkSystem.AddVirtualSwitch*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vswitch_name** | **str** |  | 
**spec** | [**HostVirtualSwitchSpec**](HostVirtualSwitchSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.add_virtual_switch_request_type import AddVirtualSwitchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddVirtualSwitchRequestType from a JSON string
add_virtual_switch_request_type_instance = AddVirtualSwitchRequestType.from_json(json)
# print the JSON string representation of the object
print AddVirtualSwitchRequestType.to_json()

# convert the object into a dict
add_virtual_switch_request_type_dict = add_virtual_switch_request_type_instance.to_dict()
# create an instance of AddVirtualSwitchRequestType from a dict
add_virtual_switch_request_type_form_dict = add_virtual_switch_request_type.from_dict(add_virtual_switch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


