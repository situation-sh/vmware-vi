# CreateClusterExRequestType

The parameters of *Folder.CreateClusterEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the new cluster.  | 
**spec** | [**ClusterConfigSpecEx**](ClusterConfigSpecEx.md) |  | 

## Example

```python
from vmware_vi.models.create_cluster_ex_request_type import CreateClusterExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterExRequestType from a JSON string
create_cluster_ex_request_type_instance = CreateClusterExRequestType.from_json(json)
# print the JSON string representation of the object
print CreateClusterExRequestType.to_json()

# convert the object into a dict
create_cluster_ex_request_type_dict = create_cluster_ex_request_type_instance.to_dict()
# create an instance of CreateClusterExRequestType from a dict
create_cluster_ex_request_type_form_dict = create_cluster_ex_request_type.from_dict(create_cluster_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


