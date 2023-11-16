# ClusterDrsVmConfigInfo

DRS configuration for a single virtual machine.  This makes it possible to override the default behavior for an individual virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**enabled** | **bool** | Flag to indicate whether or not VirtualCenter is allowed to perform any DRS migration or initial placement recommendations for this virtual machine.  If this flag is false, the virtual machine is effectively excluded from DRS.  If no individual DRS specification exists for a virtual machine, this property defaults to true.  | [optional] 
**behavior** | [**DrsBehaviorEnum**](DrsBehaviorEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_drs_vm_config_info import ClusterDrsVmConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDrsVmConfigInfo from a JSON string
cluster_drs_vm_config_info_instance = ClusterDrsVmConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDrsVmConfigInfo.to_json()

# convert the object into a dict
cluster_drs_vm_config_info_dict = cluster_drs_vm_config_info_instance.to_dict()
# create an instance of ClusterDrsVmConfigInfo from a dict
cluster_drs_vm_config_info_form_dict = cluster_drs_vm_config_info.from_dict(cluster_drs_vm_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


