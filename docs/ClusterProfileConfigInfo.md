# ClusterProfileConfigInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comply_profile** | [**ComplianceProfile**](ComplianceProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_profile_config_info import ClusterProfileConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProfileConfigInfo from a JSON string
cluster_profile_config_info_instance = ClusterProfileConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterProfileConfigInfo.to_json()

# convert the object into a dict
cluster_profile_config_info_dict = cluster_profile_config_info_instance.to_dict()
# create an instance of ClusterProfileConfigInfo from a dict
cluster_profile_config_info_form_dict = cluster_profile_config_info.from_dict(cluster_profile_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


