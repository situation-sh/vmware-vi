# HbrManagerVmReplicationCapability

This data object represents the capabilities of a given *VirtualMachine*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**supported_quiesce_mode** | **str** | A string representing the current *QuiesceMode_enum* of the virtual machine.  ***Since:*** vSphere API 6.0  | 
**compression_supported** | **bool** | Flag indicating compression support on the host on which this virtual machine is running.  ***Since:*** vSphere API 6.0  | 
**max_supported_source_disk_capacity** | **int** | Maximum disk size supported (in bytes) on the host on which this virtual machine is running.  ***Since:*** vSphere API 6.0  | 
**min_rpo** | **int** | Minimum rpo supported (in minutes) on the host on which this virtual machine is running.  ***Since:*** vSphere API 6.0  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.hbr_manager_vm_replication_capability import HbrManagerVmReplicationCapability

# TODO update the JSON string below
json = "{}"
# create an instance of HbrManagerVmReplicationCapability from a JSON string
hbr_manager_vm_replication_capability_instance = HbrManagerVmReplicationCapability.from_json(json)
# print the JSON string representation of the object
print HbrManagerVmReplicationCapability.to_json()

# convert the object into a dict
hbr_manager_vm_replication_capability_dict = hbr_manager_vm_replication_capability_instance.to_dict()
# create an instance of HbrManagerVmReplicationCapability from a dict
hbr_manager_vm_replication_capability_form_dict = hbr_manager_vm_replication_capability.from_dict(hbr_manager_vm_replication_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


