# ArrayOfClusterConfigSpecEx

A boxed array of *ClusterConfigSpecEx*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterConfigSpecEx]**](ClusterConfigSpecEx.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_config_spec_ex import ArrayOfClusterConfigSpecEx

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterConfigSpecEx from a JSON string
array_of_cluster_config_spec_ex_instance = ArrayOfClusterConfigSpecEx.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterConfigSpecEx.to_json()

# convert the object into a dict
array_of_cluster_config_spec_ex_dict = array_of_cluster_config_spec_ex_instance.to_dict()
# create an instance of ArrayOfClusterConfigSpecEx from a dict
array_of_cluster_config_spec_ex_form_dict = array_of_cluster_config_spec_ex.from_dict(array_of_cluster_config_spec_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


