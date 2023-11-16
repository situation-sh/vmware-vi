# ClusterFailoverLevelAdmissionControlInfo

The current admission control related information if the cluster was configured with a FailoverLevelAdmissionControlPolicy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_failover_level** | **int** | Current failover level.  This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. This represents the current value, as opposed to desired value configured by the user.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.cluster_failover_level_admission_control_info import ClusterFailoverLevelAdmissionControlInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFailoverLevelAdmissionControlInfo from a JSON string
cluster_failover_level_admission_control_info_instance = ClusterFailoverLevelAdmissionControlInfo.from_json(json)
# print the JSON string representation of the object
print ClusterFailoverLevelAdmissionControlInfo.to_json()

# convert the object into a dict
cluster_failover_level_admission_control_info_dict = cluster_failover_level_admission_control_info_instance.to_dict()
# create an instance of ClusterFailoverLevelAdmissionControlInfo from a dict
cluster_failover_level_admission_control_info_form_dict = cluster_failover_level_admission_control_info.from_dict(cluster_failover_level_admission_control_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


