# ReplicationDiskConfigFault

A ReplicationDiskConfigFault is thrown when there is an issue with configuring disk replication properties.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the failure.  One of the above.  ***Since:*** vSphere API 5.0  | [optional] 
**vm_ref** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**key** | **int** | The disk (device) key in the parent VM for identification purposes.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.replication_disk_config_fault import ReplicationDiskConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationDiskConfigFault from a JSON string
replication_disk_config_fault_instance = ReplicationDiskConfigFault.from_json(json)
# print the JSON string representation of the object
print ReplicationDiskConfigFault.to_json()

# convert the object into a dict
replication_disk_config_fault_dict = replication_disk_config_fault_instance.to_dict()
# create an instance of ReplicationDiskConfigFault from a dict
replication_disk_config_fault_form_dict = replication_disk_config_fault.from_dict(replication_disk_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


