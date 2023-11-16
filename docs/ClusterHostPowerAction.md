# ClusterHostPowerAction

Describes a single host power action.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_type** | [**HostPowerOperationTypeEnum**](HostPowerOperationTypeEnum.md) |  | 
**power_consumption_watt** | **int** | Estimated power consumption of the host.  In case of power-on, this is the projected increase in the cluster&#39;s power consumption. In case of power off, this is the projected decrease in the cluster&#39;s power consumption  ***Since:*** VI API 2.5  | [optional] 
**cpu_capacity_mhz** | **int** | CPU capacity of the host in units of MHz.  In case of power-on action, this is the projected increase in the cluster&#39;s CPU capacity. In case of power off, this is the projected decrease in the cluster&#39;s CPU capacity.  ***Since:*** VI API 2.5  | [optional] 
**mem_capacity_mb** | **int** | Memory capacity of the host in units of MM.  In case of power-on action, this is the projected increase in the cluster&#39;s memory capacity. In case of power off, this is the projected decrease in the cluster&#39;s memory capacity.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.cluster_host_power_action import ClusterHostPowerAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHostPowerAction from a JSON string
cluster_host_power_action_instance = ClusterHostPowerAction.from_json(json)
# print the JSON string representation of the object
print ClusterHostPowerAction.to_json()

# convert the object into a dict
cluster_host_power_action_dict = cluster_host_power_action_instance.to_dict()
# create an instance of ClusterHostPowerAction from a dict
cluster_host_power_action_form_dict = cluster_host_power_action.from_dict(cluster_host_power_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


