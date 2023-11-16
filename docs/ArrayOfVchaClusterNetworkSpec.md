# ArrayOfVchaClusterNetworkSpec

A boxed array of *VchaClusterNetworkSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VchaClusterNetworkSpec]**](VchaClusterNetworkSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vcha_cluster_network_spec import ArrayOfVchaClusterNetworkSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVchaClusterNetworkSpec from a JSON string
array_of_vcha_cluster_network_spec_instance = ArrayOfVchaClusterNetworkSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVchaClusterNetworkSpec.to_json()

# convert the object into a dict
array_of_vcha_cluster_network_spec_dict = array_of_vcha_cluster_network_spec_instance.to_dict()
# create an instance of ArrayOfVchaClusterNetworkSpec from a dict
array_of_vcha_cluster_network_spec_form_dict = array_of_vcha_cluster_network_spec.from_dict(array_of_vcha_cluster_network_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


