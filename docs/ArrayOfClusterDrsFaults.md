# ArrayOfClusterDrsFaults

A boxed array of *ClusterDrsFaults*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDrsFaults]**](ClusterDrsFaults.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_drs_faults import ArrayOfClusterDrsFaults

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDrsFaults from a JSON string
array_of_cluster_drs_faults_instance = ArrayOfClusterDrsFaults.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDrsFaults.to_json()

# convert the object into a dict
array_of_cluster_drs_faults_dict = array_of_cluster_drs_faults_instance.to_dict()
# create an instance of ArrayOfClusterDrsFaults from a dict
array_of_cluster_drs_faults_form_dict = array_of_cluster_drs_faults.from_dict(array_of_cluster_drs_faults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


