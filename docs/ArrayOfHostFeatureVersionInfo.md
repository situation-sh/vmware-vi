# ArrayOfHostFeatureVersionInfo

A boxed array of *HostFeatureVersionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFeatureVersionInfo]**](HostFeatureVersionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_feature_version_info import ArrayOfHostFeatureVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFeatureVersionInfo from a JSON string
array_of_host_feature_version_info_instance = ArrayOfHostFeatureVersionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFeatureVersionInfo.to_json()

# convert the object into a dict
array_of_host_feature_version_info_dict = array_of_host_feature_version_info_instance.to_dict()
# create an instance of ArrayOfHostFeatureVersionInfo from a dict
array_of_host_feature_version_info_form_dict = array_of_host_feature_version_info.from_dict(array_of_host_feature_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


