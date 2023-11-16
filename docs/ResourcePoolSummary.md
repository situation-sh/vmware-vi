# ResourcePoolSummary

This data object type encapsulates a typical set of resource pool information that is useful for list views and summary pages. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of resource pool.  | 
**config** | [**ResourceConfigSpec**](ResourceConfigSpec.md) |  | 
**runtime** | [**ResourcePoolRuntimeInfo**](ResourcePoolRuntimeInfo.md) |  | 
**quick_stats** | [**ResourcePoolQuickStats**](ResourcePoolQuickStats.md) |  | [optional] 
**configured_memory_mb** | **int** | Total configured memory of all virtual machines in the resource pool, in MB.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.resource_pool_summary import ResourcePoolSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolSummary from a JSON string
resource_pool_summary_instance = ResourcePoolSummary.from_json(json)
# print the JSON string representation of the object
print ResourcePoolSummary.to_json()

# convert the object into a dict
resource_pool_summary_dict = resource_pool_summary_instance.to_dict()
# create an instance of ResourcePoolSummary from a dict
resource_pool_summary_form_dict = resource_pool_summary.from_dict(resource_pool_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


