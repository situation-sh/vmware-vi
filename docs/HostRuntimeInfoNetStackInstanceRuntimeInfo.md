# HostRuntimeInfoNetStackInstanceRuntimeInfo

This data type describes network stack instance runtime info  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_stack_instance_key** | **str** | Key of the instance  ***Since:*** vSphere API 5.5  | 
**state** | **str** | State of the instance See *HostRuntimeInfoNetStackInstanceRuntimeInfoState_enum* for valid values.  ***Since:*** vSphere API 5.5  | [optional] 
**vmknic_keys** | **List[str]** | The keys of vmknics that are using this stack  ***Since:*** vSphere API 5.5  | [optional] 
**max_number_of_connections** | **int** | The maximum number of socket connections can be worked on this instance currently after booting up.  ***Since:*** vSphere API 5.5  | [optional] 
**current_ip_v6_enabled** | **bool** | If true then dual IPv4/IPv6 stack enabled else IPv4 only.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.host_runtime_info_net_stack_instance_runtime_info import HostRuntimeInfoNetStackInstanceRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostRuntimeInfoNetStackInstanceRuntimeInfo from a JSON string
host_runtime_info_net_stack_instance_runtime_info_instance = HostRuntimeInfoNetStackInstanceRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print HostRuntimeInfoNetStackInstanceRuntimeInfo.to_json()

# convert the object into a dict
host_runtime_info_net_stack_instance_runtime_info_dict = host_runtime_info_net_stack_instance_runtime_info_instance.to_dict()
# create an instance of HostRuntimeInfoNetStackInstanceRuntimeInfo from a dict
host_runtime_info_net_stack_instance_runtime_info_form_dict = host_runtime_info_net_stack_instance_runtime_info.from_dict(host_runtime_info_net_stack_instance_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


