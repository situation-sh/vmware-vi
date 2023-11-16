# CannotPowerOffVmInCluster

This fault is reported when a user attempts to power off or suspend a VM when the HA master agent to which vCenter Server is connected does not manage the VM.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation being performed.  Values come from *CannotPowerOffVmInClusterOperation_enum*.  ***Since:*** vSphere API 5.0  | 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | Name of the Virtual Machine  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.cannot_power_off_vm_in_cluster import CannotPowerOffVmInCluster

# TODO update the JSON string below
json = "{}"
# create an instance of CannotPowerOffVmInCluster from a JSON string
cannot_power_off_vm_in_cluster_instance = CannotPowerOffVmInCluster.from_json(json)
# print the JSON string representation of the object
print CannotPowerOffVmInCluster.to_json()

# convert the object into a dict
cannot_power_off_vm_in_cluster_dict = cannot_power_off_vm_in_cluster_instance.to_dict()
# create an instance of CannotPowerOffVmInCluster from a dict
cannot_power_off_vm_in_cluster_form_dict = cannot_power_off_vm_in_cluster.from_dict(cannot_power_off_vm_in_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


