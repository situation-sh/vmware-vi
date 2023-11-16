# DistributedVirtualSwitchManagerImportResult

The *DistributedVirtualSwitchManagerImportResult* data object represents the results of a *DistributedVirtualSwitchManager.DVSManagerImportEntity_Task* operation.  It contains lists of the switches and portgroups that were created. It also contains a list of faults that occurred during the operation.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distributed_virtual_switch** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of distributed virtual switches.  ***Since:*** vSphere API 5.1  Refers instances of *DistributedVirtualSwitch*.  | [optional] 
**distributed_virtual_portgroup** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of distributed virtual portgroups.  ***Since:*** vSphere API 5.1  Refers instances of *DistributedVirtualPortgroup*.  | [optional] 
**import_fault** | [**List[ImportOperationBulkFaultFaultOnImport]**](ImportOperationBulkFaultFaultOnImport.md) | Faults that occurred on the entities during the import operation.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_manager_import_result import DistributedVirtualSwitchManagerImportResult

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchManagerImportResult from a JSON string
distributed_virtual_switch_manager_import_result_instance = DistributedVirtualSwitchManagerImportResult.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchManagerImportResult.to_json()

# convert the object into a dict
distributed_virtual_switch_manager_import_result_dict = distributed_virtual_switch_manager_import_result_instance.to_dict()
# create an instance of DistributedVirtualSwitchManagerImportResult from a dict
distributed_virtual_switch_manager_import_result_form_dict = distributed_virtual_switch_manager_import_result.from_dict(distributed_virtual_switch_manager_import_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


