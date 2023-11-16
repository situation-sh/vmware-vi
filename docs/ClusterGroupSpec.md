# ClusterGroupSpec

An incremental update to the cluster-wide groups.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ClusterGroupInfo**](ClusterGroupInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_group_spec import ClusterGroupSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGroupSpec from a JSON string
cluster_group_spec_instance = ClusterGroupSpec.from_json(json)
# print the JSON string representation of the object
print ClusterGroupSpec.to_json()

# convert the object into a dict
cluster_group_spec_dict = cluster_group_spec_instance.to_dict()
# create an instance of ClusterGroupSpec from a dict
cluster_group_spec_form_dict = cluster_group_spec.from_dict(cluster_group_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


