# DistributedVirtualSwitchHostMemberRuntimeState

Runtime state of a host member.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_max_proxy_switch_ports** | **int** | Current maximum number of ports allowed to be created in the proxy switch.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_host_member_runtime_state import DistributedVirtualSwitchHostMemberRuntimeState

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchHostMemberRuntimeState from a JSON string
distributed_virtual_switch_host_member_runtime_state_instance = DistributedVirtualSwitchHostMemberRuntimeState.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchHostMemberRuntimeState.to_json()

# convert the object into a dict
distributed_virtual_switch_host_member_runtime_state_dict = distributed_virtual_switch_host_member_runtime_state_instance.to_dict()
# create an instance of DistributedVirtualSwitchHostMemberRuntimeState from a dict
distributed_virtual_switch_host_member_runtime_state_form_dict = distributed_virtual_switch_host_member_runtime_state.from_dict(distributed_virtual_switch_host_member_runtime_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


