# RemoveVirtualSwitchRequestType

The parameters of *HostNetworkSystem.RemoveVirtualSwitch*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vswitch_name** | **str** |  | 

## Example

```python
from vmware_vi.models.remove_virtual_switch_request_type import RemoveVirtualSwitchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveVirtualSwitchRequestType from a JSON string
remove_virtual_switch_request_type_instance = RemoveVirtualSwitchRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveVirtualSwitchRequestType.to_json()

# convert the object into a dict
remove_virtual_switch_request_type_dict = remove_virtual_switch_request_type_instance.to_dict()
# create an instance of RemoveVirtualSwitchRequestType from a dict
remove_virtual_switch_request_type_form_dict = remove_virtual_switch_request_type.from_dict(remove_virtual_switch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


