# ExtensionManagerIpAllocationUsage

This data object type contains usage information about an extension's IP allocation usage.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | Key of the extension whose usage is being reported.  ***Since:*** vSphere API 5.1  | 
**num_addresses** | **int** | Number of IP addresses allocated from IP pools.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.extension_manager_ip_allocation_usage import ExtensionManagerIpAllocationUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionManagerIpAllocationUsage from a JSON string
extension_manager_ip_allocation_usage_instance = ExtensionManagerIpAllocationUsage.from_json(json)
# print the JSON string representation of the object
print ExtensionManagerIpAllocationUsage.to_json()

# convert the object into a dict
extension_manager_ip_allocation_usage_dict = extension_manager_ip_allocation_usage_instance.to_dict()
# create an instance of ExtensionManagerIpAllocationUsage from a dict
extension_manager_ip_allocation_usage_form_dict = extension_manager_ip_allocation_usage.from_dict(extension_manager_ip_allocation_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


