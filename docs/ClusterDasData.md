# ClusterDasData

Base class for DAS data for high availability service for a cluster.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cluster_das_data import ClusterDasData

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasData from a JSON string
cluster_das_data_instance = ClusterDasData.from_json(json)
# print the JSON string representation of the object
print ClusterDasData.to_json()

# convert the object into a dict
cluster_das_data_dict = cluster_das_data_instance.to_dict()
# create an instance of ClusterDasData from a dict
cluster_das_data_form_dict = cluster_das_data.from_dict(cluster_das_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


