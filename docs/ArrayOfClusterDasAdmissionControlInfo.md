# ArrayOfClusterDasAdmissionControlInfo

A boxed array of *ClusterDasAdmissionControlInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDasAdmissionControlInfo]**](ClusterDasAdmissionControlInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_das_admission_control_info import ArrayOfClusterDasAdmissionControlInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDasAdmissionControlInfo from a JSON string
array_of_cluster_das_admission_control_info_instance = ArrayOfClusterDasAdmissionControlInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDasAdmissionControlInfo.to_json()

# convert the object into a dict
array_of_cluster_das_admission_control_info_dict = array_of_cluster_das_admission_control_info_instance.to_dict()
# create an instance of ArrayOfClusterDasAdmissionControlInfo from a dict
array_of_cluster_das_admission_control_info_form_dict = array_of_cluster_das_admission_control_info.from_dict(array_of_cluster_das_admission_control_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


