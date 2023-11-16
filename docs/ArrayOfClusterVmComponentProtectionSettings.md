# ArrayOfClusterVmComponentProtectionSettings

A boxed array of *ClusterVmComponentProtectionSettings*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterVmComponentProtectionSettings]**](ClusterVmComponentProtectionSettings.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_vm_component_protection_settings import ArrayOfClusterVmComponentProtectionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterVmComponentProtectionSettings from a JSON string
array_of_cluster_vm_component_protection_settings_instance = ArrayOfClusterVmComponentProtectionSettings.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterVmComponentProtectionSettings.to_json()

# convert the object into a dict
array_of_cluster_vm_component_protection_settings_dict = array_of_cluster_vm_component_protection_settings_instance.to_dict()
# create an instance of ArrayOfClusterVmComponentProtectionSettings from a dict
array_of_cluster_vm_component_protection_settings_form_dict = array_of_cluster_vm_component_protection_settings.from_dict(array_of_cluster_vm_component_protection_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


