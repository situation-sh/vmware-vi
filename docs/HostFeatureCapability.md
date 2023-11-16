# HostFeatureCapability

A feature that the host is able to provide at a particular value.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Accessor name to the feature capability.  ***Since:*** vSphere API 5.1  | 
**feature_name** | **str** | Name of the feature.  Identical to the key.  ***Since:*** vSphere API 5.1  | 
**value** | **str** | Opaque value that the feature is capable at.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_feature_capability import HostFeatureCapability

# TODO update the JSON string below
json = "{}"
# create an instance of HostFeatureCapability from a JSON string
host_feature_capability_instance = HostFeatureCapability.from_json(json)
# print the JSON string representation of the object
print HostFeatureCapability.to_json()

# convert the object into a dict
host_feature_capability_dict = host_feature_capability_instance.to_dict()
# create an instance of HostFeatureCapability from a dict
host_feature_capability_form_dict = host_feature_capability.from_dict(host_feature_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


