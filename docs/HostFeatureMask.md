# HostFeatureMask

A mask that is applied to a host feature capability.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Accessor name to the feature mask.  ***Since:*** vSphere API 5.1  | 
**feature_name** | **str** | Name of the feature Identical to the key.  ***Since:*** vSphere API 5.1  | 
**value** | **str** | Opaque value to change the host feature capability to.  Masking operation is contained in the value.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_feature_mask import HostFeatureMask

# TODO update the JSON string below
json = "{}"
# create an instance of HostFeatureMask from a JSON string
host_feature_mask_instance = HostFeatureMask.from_json(json)
# print the JSON string representation of the object
print HostFeatureMask.to_json()

# convert the object into a dict
host_feature_mask_dict = host_feature_mask_instance.to_dict()
# create an instance of HostFeatureMask from a dict
host_feature_mask_form_dict = host_feature_mask.from_dict(host_feature_mask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


