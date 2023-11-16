# ArrayOfDistributedVirtualSwitchHostMemberConfigSpec

A boxed array of *DistributedVirtualSwitchHostMemberConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchHostMemberConfigSpec]**](DistributedVirtualSwitchHostMemberConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_host_member_config_spec import ArrayOfDistributedVirtualSwitchHostMemberConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchHostMemberConfigSpec from a JSON string
array_of_distributed_virtual_switch_host_member_config_spec_instance = ArrayOfDistributedVirtualSwitchHostMemberConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchHostMemberConfigSpec.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_host_member_config_spec_dict = array_of_distributed_virtual_switch_host_member_config_spec_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchHostMemberConfigSpec from a dict
array_of_distributed_virtual_switch_host_member_config_spec_form_dict = array_of_distributed_virtual_switch_host_member_config_spec.from_dict(array_of_distributed_virtual_switch_host_member_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


