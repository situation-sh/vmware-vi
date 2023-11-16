# ArrayOfDistributedVirtualSwitchHostMember

A boxed array of *DistributedVirtualSwitchHostMember*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchHostMember]**](DistributedVirtualSwitchHostMember.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_host_member import ArrayOfDistributedVirtualSwitchHostMember

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchHostMember from a JSON string
array_of_distributed_virtual_switch_host_member_instance = ArrayOfDistributedVirtualSwitchHostMember.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchHostMember.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_host_member_dict = array_of_distributed_virtual_switch_host_member_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchHostMember from a dict
array_of_distributed_virtual_switch_host_member_form_dict = array_of_distributed_virtual_switch_host_member.from_dict(array_of_distributed_virtual_switch_host_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


