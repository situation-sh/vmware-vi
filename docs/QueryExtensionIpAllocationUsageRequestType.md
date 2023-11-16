# QueryExtensionIpAllocationUsageRequestType

The parameters of *ExtensionManager.QueryExtensionIpAllocationUsage*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_keys** | **List[str]** | List of extensions whose IP allocation is being queried. If no extension keys are specified then allocation data for all registered extensions are returned.  | [optional] 

## Example

```python
from vmware_vi.models.query_extension_ip_allocation_usage_request_type import QueryExtensionIpAllocationUsageRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryExtensionIpAllocationUsageRequestType from a JSON string
query_extension_ip_allocation_usage_request_type_instance = QueryExtensionIpAllocationUsageRequestType.from_json(json)
# print the JSON string representation of the object
print QueryExtensionIpAllocationUsageRequestType.to_json()

# convert the object into a dict
query_extension_ip_allocation_usage_request_type_dict = query_extension_ip_allocation_usage_request_type_instance.to_dict()
# create an instance of QueryExtensionIpAllocationUsageRequestType from a dict
query_extension_ip_allocation_usage_request_type_form_dict = query_extension_ip_allocation_usage_request_type.from_dict(query_extension_ip_allocation_usage_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


