# VsanUpgradeSystemNetworkPartitionInfo

Information about a particular group of hosts making up a network partition.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Hosts that make up the network partition  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_network_partition_info import VsanUpgradeSystemNetworkPartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemNetworkPartitionInfo from a JSON string
vsan_upgrade_system_network_partition_info_instance = VsanUpgradeSystemNetworkPartitionInfo.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemNetworkPartitionInfo.to_json()

# convert the object into a dict
vsan_upgrade_system_network_partition_info_dict = vsan_upgrade_system_network_partition_info_instance.to_dict()
# create an instance of VsanUpgradeSystemNetworkPartitionInfo from a dict
vsan_upgrade_system_network_partition_info_form_dict = vsan_upgrade_system_network_partition_info.from_dict(vsan_upgrade_system_network_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


