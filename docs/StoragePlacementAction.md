# StoragePlacementAction

Describes a single storage initial placement action for placing a virtual machine or a set of virtual disks on a datastore.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**relocate_spec** | [**VirtualMachineRelocateSpec**](VirtualMachineRelocateSpec.md) |  | 
**destination** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**space_util_before** | **float** | Current space utilization on the target datastore.  Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.  ***Since:*** vSphere API 5.0  | [optional] 
**space_demand_before** | **float** | Current space demand on the target datastore.  Unit: percentage. For example, if set to 70.0, space demand is 70%. This value include the space demanded by thin provisioned VMs. Hence, it may be higher than 100%. If not set, the value is not available.  ***Since:*** vSphere API 6.0  | [optional] 
**space_util_after** | **float** | Space utilization on the target datastore after placing the virtual disk.  Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.  ***Since:*** vSphere API 5.0  | [optional] 
**space_demand_after** | **float** | Space demand on the target datastore after placing the virtual disk.  Unit: percentage. For example, if set to 70.0, space demand is 70%. This value include the space demanded by thin provisioned VMs. Hence, it may be higher than 100%. If not set, the value is not available.  ***Since:*** vSphere API 6.0  | [optional] 
**io_latency_before** | **float** | Current I/O latency on the target datastore.  Unit: millisecond. If not set, the value is not available.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_placement_action import StoragePlacementAction

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePlacementAction from a JSON string
storage_placement_action_instance = StoragePlacementAction.from_json(json)
# print the JSON string representation of the object
print StoragePlacementAction.to_json()

# convert the object into a dict
storage_placement_action_dict = storage_placement_action_instance.to_dict()
# create an instance of StoragePlacementAction from a dict
storage_placement_action_form_dict = storage_placement_action.from_dict(storage_placement_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


