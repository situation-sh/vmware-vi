# IncompatibleHostForVmReplication

A IncompatibleHostForVmReplication is thrown when a VM is powered on or migrated to a host which does not support the replication configuration of the VM.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | The VM which has replication configured  ***Since:*** vSphere API 6.0  | 
**host_name** | **str** | The host which is incompatible for VM replication  ***Since:*** vSphere API 6.0  | 
**reason** | **str** | The reason why the host is incompatible  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.incompatible_host_for_vm_replication import IncompatibleHostForVmReplication

# TODO update the JSON string below
json = "{}"
# create an instance of IncompatibleHostForVmReplication from a JSON string
incompatible_host_for_vm_replication_instance = IncompatibleHostForVmReplication.from_json(json)
# print the JSON string representation of the object
print IncompatibleHostForVmReplication.to_json()

# convert the object into a dict
incompatible_host_for_vm_replication_dict = incompatible_host_for_vm_replication_instance.to_dict()
# create an instance of IncompatibleHostForVmReplication from a dict
incompatible_host_for_vm_replication_form_dict = incompatible_host_for_vm_replication.from_dict(incompatible_host_for_vm_replication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


