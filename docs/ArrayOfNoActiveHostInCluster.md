# ArrayOfNoActiveHostInCluster

A boxed array of *NoActiveHostInCluster*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoActiveHostInCluster]**](NoActiveHostInCluster.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_active_host_in_cluster import ArrayOfNoActiveHostInCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoActiveHostInCluster from a JSON string
array_of_no_active_host_in_cluster_instance = ArrayOfNoActiveHostInCluster.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoActiveHostInCluster.to_json()

# convert the object into a dict
array_of_no_active_host_in_cluster_dict = array_of_no_active_host_in_cluster_instance.to_dict()
# create an instance of ArrayOfNoActiveHostInCluster from a dict
array_of_no_active_host_in_cluster_form_dict = array_of_no_active_host_in_cluster.from_dict(array_of_no_active_host_in_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


