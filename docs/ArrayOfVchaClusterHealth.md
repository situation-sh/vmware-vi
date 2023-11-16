# ArrayOfVchaClusterHealth

A boxed array of *VchaClusterHealth*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VchaClusterHealth]**](VchaClusterHealth.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vcha_cluster_health import ArrayOfVchaClusterHealth

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVchaClusterHealth from a JSON string
array_of_vcha_cluster_health_instance = ArrayOfVchaClusterHealth.from_json(json)
# print the JSON string representation of the object
print ArrayOfVchaClusterHealth.to_json()

# convert the object into a dict
array_of_vcha_cluster_health_dict = array_of_vcha_cluster_health_instance.to_dict()
# create an instance of ArrayOfVchaClusterHealth from a dict
array_of_vcha_cluster_health_form_dict = array_of_vcha_cluster_health.from_dict(array_of_vcha_cluster_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


