# ClusterDasAdmissionControlInfo

Base class for admission control related information of a vSphere HA cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cluster_das_admission_control_info import ClusterDasAdmissionControlInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasAdmissionControlInfo from a JSON string
cluster_das_admission_control_info_instance = ClusterDasAdmissionControlInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasAdmissionControlInfo.to_json()

# convert the object into a dict
cluster_das_admission_control_info_dict = cluster_das_admission_control_info_instance.to_dict()
# create an instance of ClusterDasAdmissionControlInfo from a dict
cluster_das_admission_control_info_form_dict = cluster_das_admission_control_info.from_dict(cluster_das_admission_control_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


