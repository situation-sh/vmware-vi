# PerformVsanUpgradeRequestType

The parameters of *VsanUpgradeSystem.PerformVsanUpgrade_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**perform_object_upgrade** | **bool** | After all disk groups have been updated, also upgrade all objects. Once started, rollback of the on disk format is no longer possible. Object upgrade unlocks new VSAN features.  | [optional] 
**downgrade_format** | **bool** | Perform a on-disk format downgrade instead of upgrade. Only possible if no upgraded objects exist.  | [optional] 
**allow_reduced_redundancy** | **bool** | Removes the need for one disk group worth of free space, by allowing reduced redundancy during disk upgrade.  | [optional] 
**exclude_hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Internal debug option meant for functional testing of VSAN upgrades. Skips upgrade on certain hosts and implies performObjectUpgrade being false. Should not be used by customers.  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.perform_vsan_upgrade_request_type import PerformVsanUpgradeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PerformVsanUpgradeRequestType from a JSON string
perform_vsan_upgrade_request_type_instance = PerformVsanUpgradeRequestType.from_json(json)
# print the JSON string representation of the object
print PerformVsanUpgradeRequestType.to_json()

# convert the object into a dict
perform_vsan_upgrade_request_type_dict = perform_vsan_upgrade_request_type_instance.to_dict()
# create an instance of PerformVsanUpgradeRequestType from a dict
perform_vsan_upgrade_request_type_form_dict = perform_vsan_upgrade_request_type.from_dict(perform_vsan_upgrade_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


