# ArrayOfDistributedVirtualSwitchHostMemberPnicSpec

A boxed array of *DistributedVirtualSwitchHostMemberPnicSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchHostMemberPnicSpec]**](DistributedVirtualSwitchHostMemberPnicSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_host_member_pnic_spec import ArrayOfDistributedVirtualSwitchHostMemberPnicSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchHostMemberPnicSpec from a JSON string
array_of_distributed_virtual_switch_host_member_pnic_spec_instance = ArrayOfDistributedVirtualSwitchHostMemberPnicSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchHostMemberPnicSpec.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_host_member_pnic_spec_dict = array_of_distributed_virtual_switch_host_member_pnic_spec_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchHostMemberPnicSpec from a dict
array_of_distributed_virtual_switch_host_member_pnic_spec_form_dict = array_of_distributed_virtual_switch_host_member_pnic_spec.from_dict(array_of_distributed_virtual_switch_host_member_pnic_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


