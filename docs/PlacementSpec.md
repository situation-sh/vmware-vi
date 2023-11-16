# PlacementSpec

PlacementSpec encapsulates all of the information passed to the *ClusterComputeResource.PlaceVm* method, which asks DRS for recommendations for target hosts and datastores for placing a virtual machine and its virtual disks in a cluster using unified VMotion.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**VirtualMachineMovePriorityEnum**](VirtualMachineMovePriorityEnum.md) |  | [optional] 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**config_spec** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | [optional] 
**relocate_spec** | [**VirtualMachineRelocateSpec**](VirtualMachineRelocateSpec.md) |  | [optional] 
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | A list of compatible hosts for the virtual machine.  This list is ignored if relocateSpec.host is set. For both intra-vCenter and cross-vCenter migrations, this list is required if relocateSpec.host is unset. If neither relocateSpec.host nor a list of compatible hosts are specified, all hosts in the cluster will be considered, in which case, the selected hosts in the PlacementResult are not guaranteed to be compatible with the incoming virtual machine.  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | [optional] 
**datastores** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | A list of compatible datastores for the virtual machine.  This list is ignored if relocateSpec.datastore is set. For both intra-vCenter and cross-vCenter migrations, this list is required if relocateSpec.datastore is unset. If neither relocateSpec.datastore nor a list of compatible datastores are specified, all datastores connected to hosts in the cluster will be considered, in which case, the selected datastores in the PlacementResult are not guaranteed to be compatible with the incoming virtual machine.  ***Since:*** vSphere API 6.0  Refers instances of *Datastore*.  | [optional] 
**storage_pods** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | A list of compatible datastore clusters for the virtual machine.  This list is ignored if relocateSpec.datastore is set. For both intra-vCenter and cross-vCenter migrations, this list can be empty, in which case, the user should set either RelocateSpec.datastore or PlacementSpec.datastores as the target datastore or the list of compatible datastores.  ***Since:*** vSphere API 6.0  Refers instances of *StoragePod*.  | [optional] 
**disallow_prerequisite_moves** | **bool** | Specification for whether to disable pre-requisite vmotions or storage vmotions for virtual machine placement.  The default value is true, that is, to disallow such prerequisite moves.  ***Since:*** vSphere API 6.0  | [optional] 
**rules** | [**List[ClusterRuleInfo]**](ClusterRuleInfo.md) | A list of rules to respect while placing the virtual machine on target cluster.  If the list is empty, rules will not be considered during placement, in case of cross-cluster placement within a VC and cross VC placement across VCs.  ***Since:*** vSphere API 6.0  | [optional] 
**key** | **str** | Client generated identifier as a reference to the placement request  ***Since:*** vSphere API 6.0  | [optional] 
**placement_type** | **str** | Type of the placement.  The set of possible values are described in *PlacementSpecPlacementType_enum*  ***Since:*** vSphere API 6.0  | [optional] 
**clone_spec** | [**VirtualMachineCloneSpec**](VirtualMachineCloneSpec.md) |  | [optional] 
**clone_name** | **str** | Name for the cloned virtual machine, if the operation type is a clone  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.placement_spec import PlacementSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementSpec from a JSON string
placement_spec_instance = PlacementSpec.from_json(json)
# print the JSON string representation of the object
print PlacementSpec.to_json()

# convert the object into a dict
placement_spec_dict = placement_spec_instance.to_dict()
# create an instance of PlacementSpec from a dict
placement_spec_form_dict = placement_spec.from_dict(placement_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


