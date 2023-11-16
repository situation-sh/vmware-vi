# VsanUpgradeSystemNetworkPartitionIssue

Pre-flight check encountered a network partition.  Contains details about the discovered network partition.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitions** | [**List[VsanUpgradeSystemNetworkPartitionInfo]**](VsanUpgradeSystemNetworkPartitionInfo.md) | List of network partitions  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_network_partition_issue import VsanUpgradeSystemNetworkPartitionIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemNetworkPartitionIssue from a JSON string
vsan_upgrade_system_network_partition_issue_instance = VsanUpgradeSystemNetworkPartitionIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemNetworkPartitionIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_network_partition_issue_dict = vsan_upgrade_system_network_partition_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemNetworkPartitionIssue from a dict
vsan_upgrade_system_network_partition_issue_form_dict = vsan_upgrade_system_network_partition_issue.from_dict(vsan_upgrade_system_network_partition_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


