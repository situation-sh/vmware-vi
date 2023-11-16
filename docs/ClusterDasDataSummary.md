# ClusterDasDataSummary

This class contains the summary of the data that DAS needs/uses.  The actual data is available in *ClusterDasDataDetails* and can be retrieved using the *ClusterComputeResource.RetrieveDasData* method. This class is meant for VMware internal use only.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_list_version** | **int** | The version corresponding to the hostList  ***Since:*** vSphere API 5.0  | 
**cluster_config_version** | **int** | The version corresponding to the clusterConfig  ***Since:*** vSphere API 5.0  | 
**compat_list_version** | **int** | The version corresponding to the compatList  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.cluster_das_data_summary import ClusterDasDataSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasDataSummary from a JSON string
cluster_das_data_summary_instance = ClusterDasDataSummary.from_json(json)
# print the JSON string representation of the object
print ClusterDasDataSummary.to_json()

# convert the object into a dict
cluster_das_data_summary_dict = cluster_das_data_summary_instance.to_dict()
# create an instance of ClusterDasDataSummary from a dict
cluster_das_data_summary_form_dict = cluster_das_data_summary.from_dict(cluster_das_data_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


