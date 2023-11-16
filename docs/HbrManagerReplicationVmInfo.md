# HbrManagerReplicationVmInfo

This data object represents the essential information about the state of a given replicated *VirtualMachine*.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | A string representing the current *ReplicationVmState_enum* of the virtual machine.  ***Since:*** vSphere API 5.0  | 
**progress_info** | [**ReplicationVmProgressInfo**](ReplicationVmProgressInfo.md) |  | [optional] 
**image_id** | **str** | An optional imageId that identifies the instance being created, this is the imagId string that is passed to *HbrManager.HbrCreateInstance_Task* or *HbrManager.HbrStartOfflineInstance_Task*  ***Since:*** vSphere API 5.0  | [optional] 
**last_error** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.hbr_manager_replication_vm_info import HbrManagerReplicationVmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HbrManagerReplicationVmInfo from a JSON string
hbr_manager_replication_vm_info_instance = HbrManagerReplicationVmInfo.from_json(json)
# print the JSON string representation of the object
print HbrManagerReplicationVmInfo.to_json()

# convert the object into a dict
hbr_manager_replication_vm_info_dict = hbr_manager_replication_vm_info_instance.to_dict()
# create an instance of HbrManagerReplicationVmInfo from a dict
hbr_manager_replication_vm_info_form_dict = hbr_manager_replication_vm_info.from_dict(hbr_manager_replication_vm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


