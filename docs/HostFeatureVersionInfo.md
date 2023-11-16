# HostFeatureVersionInfo

Feature-specific version information for a host  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key that identifies a feature, list of possible values are specified in *HostFeatureVersionKey_enum*  ***Since:*** vSphere API 4.1  | 
**value** | **str** | The version string of this feature  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.host_feature_version_info import HostFeatureVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostFeatureVersionInfo from a JSON string
host_feature_version_info_instance = HostFeatureVersionInfo.from_json(json)
# print the JSON string representation of the object
print HostFeatureVersionInfo.to_json()

# convert the object into a dict
host_feature_version_info_dict = host_feature_version_info_instance.to_dict()
# create an instance of HostFeatureVersionInfo from a dict
host_feature_version_info_form_dict = host_feature_version_info.from_dict(host_feature_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


