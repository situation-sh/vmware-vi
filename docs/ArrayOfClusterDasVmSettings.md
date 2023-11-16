# ArrayOfClusterDasVmSettings

A boxed array of *ClusterDasVmSettings*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDasVmSettings]**](ClusterDasVmSettings.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_das_vm_settings import ArrayOfClusterDasVmSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDasVmSettings from a JSON string
array_of_cluster_das_vm_settings_instance = ArrayOfClusterDasVmSettings.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDasVmSettings.to_json()

# convert the object into a dict
array_of_cluster_das_vm_settings_dict = array_of_cluster_das_vm_settings_instance.to_dict()
# create an instance of ArrayOfClusterDasVmSettings from a dict
array_of_cluster_das_vm_settings_form_dict = array_of_cluster_das_vm_settings.from_dict(array_of_cluster_das_vm_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


