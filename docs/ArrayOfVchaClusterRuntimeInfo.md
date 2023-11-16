# ArrayOfVchaClusterRuntimeInfo

A boxed array of *VchaClusterRuntimeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VchaClusterRuntimeInfo]**](VchaClusterRuntimeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vcha_cluster_runtime_info import ArrayOfVchaClusterRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVchaClusterRuntimeInfo from a JSON string
array_of_vcha_cluster_runtime_info_instance = ArrayOfVchaClusterRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVchaClusterRuntimeInfo.to_json()

# convert the object into a dict
array_of_vcha_cluster_runtime_info_dict = array_of_vcha_cluster_runtime_info_instance.to_dict()
# create an instance of ArrayOfVchaClusterRuntimeInfo from a dict
array_of_vcha_cluster_runtime_info_form_dict = array_of_vcha_cluster_runtime_info.from_dict(array_of_vcha_cluster_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


