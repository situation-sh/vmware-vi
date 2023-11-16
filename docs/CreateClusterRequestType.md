# CreateClusterRequestType

The parameters of *Folder.CreateCluster*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the new cluster.  | 
**spec** | [**ClusterConfigSpec**](ClusterConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_cluster_request_type import CreateClusterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterRequestType from a JSON string
create_cluster_request_type_instance = CreateClusterRequestType.from_json(json)
# print the JSON string representation of the object
print CreateClusterRequestType.to_json()

# convert the object into a dict
create_cluster_request_type_dict = create_cluster_request_type_instance.to_dict()
# create an instance of CreateClusterRequestType from a dict
create_cluster_request_type_form_dict = create_cluster_request_type.from_dict(create_cluster_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


