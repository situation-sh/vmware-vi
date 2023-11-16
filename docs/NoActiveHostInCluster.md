# NoActiveHostInCluster

A NoActiveHostInCluster fault is thrown when there is no host in a valid state in the given compute resource to perform a specified operation.  This can happen, for example, if all the hosts are disconnected or in maintenance mode. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_resource** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.no_active_host_in_cluster import NoActiveHostInCluster

# TODO update the JSON string below
json = "{}"
# create an instance of NoActiveHostInCluster from a JSON string
no_active_host_in_cluster_instance = NoActiveHostInCluster.from_json(json)
# print the JSON string representation of the object
print NoActiveHostInCluster.to_json()

# convert the object into a dict
no_active_host_in_cluster_dict = no_active_host_in_cluster_instance.to_dict()
# create an instance of NoActiveHostInCluster from a dict
no_active_host_in_cluster_form_dict = no_active_host_in_cluster.from_dict(no_active_host_in_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


