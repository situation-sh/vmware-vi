# ArrayOfHostFeatureMask

A boxed array of *HostFeatureMask*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFeatureMask]**](HostFeatureMask.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_feature_mask import ArrayOfHostFeatureMask

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFeatureMask from a JSON string
array_of_host_feature_mask_instance = ArrayOfHostFeatureMask.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFeatureMask.to_json()

# convert the object into a dict
array_of_host_feature_mask_dict = array_of_host_feature_mask_instance.to_dict()
# create an instance of ArrayOfHostFeatureMask from a dict
array_of_host_feature_mask_form_dict = array_of_host_feature_mask.from_dict(array_of_host_feature_mask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


