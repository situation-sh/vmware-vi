# DVSManagerDvsConfigTarget

Configuration specification for a DistributedVirtualSwitch or DistributedVirtualPortgroup.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distributed_virtual_portgroup** | [**List[DistributedVirtualPortgroupInfo]**](DistributedVirtualPortgroupInfo.md) | List of any DistributedVirtualPortgroup available for host Virtual NIC connection.  ***Since:*** vSphere API 4.0  | [optional] 
**distributed_virtual_switch** | [**List[DistributedVirtualSwitchInfo]**](DistributedVirtualSwitchInfo.md) | List of any DistributedVirtualSwitch available for host Virtual NIC connection.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_manager_dvs_config_target import DVSManagerDvsConfigTarget

# TODO update the JSON string below
json = "{}"
# create an instance of DVSManagerDvsConfigTarget from a JSON string
dvs_manager_dvs_config_target_instance = DVSManagerDvsConfigTarget.from_json(json)
# print the JSON string representation of the object
print DVSManagerDvsConfigTarget.to_json()

# convert the object into a dict
dvs_manager_dvs_config_target_dict = dvs_manager_dvs_config_target_instance.to_dict()
# create an instance of DVSManagerDvsConfigTarget from a dict
dvs_manager_dvs_config_target_form_dict = dvs_manager_dvs_config_target.from_dict(dvs_manager_dvs_config_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


