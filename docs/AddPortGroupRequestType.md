# AddPortGroupRequestType

The parameters of *HostNetworkSystem.AddPortGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portgrp** | [**HostPortGroupSpec**](HostPortGroupSpec.md) |  | 

## Example

```python
from vmware_vi.models.add_port_group_request_type import AddPortGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddPortGroupRequestType from a JSON string
add_port_group_request_type_instance = AddPortGroupRequestType.from_json(json)
# print the JSON string representation of the object
print AddPortGroupRequestType.to_json()

# convert the object into a dict
add_port_group_request_type_dict = add_port_group_request_type_instance.to_dict()
# create an instance of AddPortGroupRequestType from a dict
add_port_group_request_type_form_dict = add_port_group_request_type.from_dict(add_port_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


