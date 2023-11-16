# UpdatePortGroupRequestType

The parameters of *HostNetworkSystem.UpdatePortGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pg_name** | **str** |  | 
**portgrp** | [**HostPortGroupSpec**](HostPortGroupSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_port_group_request_type import UpdatePortGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePortGroupRequestType from a JSON string
update_port_group_request_type_instance = UpdatePortGroupRequestType.from_json(json)
# print the JSON string representation of the object
print UpdatePortGroupRequestType.to_json()

# convert the object into a dict
update_port_group_request_type_dict = update_port_group_request_type_instance.to_dict()
# create an instance of UpdatePortGroupRequestType from a dict
update_port_group_request_type_form_dict = update_port_group_request_type.from_dict(update_port_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


