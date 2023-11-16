# ClusterDatastoreUpdateSpec

An incremental update to a Datastore list.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_datastore_update_spec import ClusterDatastoreUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDatastoreUpdateSpec from a JSON string
cluster_datastore_update_spec_instance = ClusterDatastoreUpdateSpec.from_json(json)
# print the JSON string representation of the object
print ClusterDatastoreUpdateSpec.to_json()

# convert the object into a dict
cluster_datastore_update_spec_dict = cluster_datastore_update_spec_instance.to_dict()
# create an instance of ClusterDatastoreUpdateSpec from a dict
cluster_datastore_update_spec_form_dict = cluster_datastore_update_spec.from_dict(cluster_datastore_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


