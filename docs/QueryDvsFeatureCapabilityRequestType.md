# QueryDvsFeatureCapabilityRequestType

The parameters of *DistributedVirtualSwitchManager.QueryDvsFeatureCapability*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_product_spec** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_dvs_feature_capability_request_type import QueryDvsFeatureCapabilityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDvsFeatureCapabilityRequestType from a JSON string
query_dvs_feature_capability_request_type_instance = QueryDvsFeatureCapabilityRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDvsFeatureCapabilityRequestType.to_json()

# convert the object into a dict
query_dvs_feature_capability_request_type_dict = query_dvs_feature_capability_request_type_instance.to_dict()
# create an instance of QueryDvsFeatureCapabilityRequestType from a dict
query_dvs_feature_capability_request_type_form_dict = query_dvs_feature_capability_request_type.from_dict(query_dvs_feature_capability_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


