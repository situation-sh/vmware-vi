# ArrayOfClusterDasData

A boxed array of *ClusterDasData*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDasData]**](ClusterDasData.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_das_data import ArrayOfClusterDasData

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDasData from a JSON string
array_of_cluster_das_data_instance = ArrayOfClusterDasData.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDasData.to_json()

# convert the object into a dict
array_of_cluster_das_data_dict = array_of_cluster_das_data_instance.to_dict()
# create an instance of ArrayOfClusterDasData from a dict
array_of_cluster_das_data_form_dict = array_of_cluster_das_data.from_dict(array_of_cluster_das_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


