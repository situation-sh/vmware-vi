# ResourcePoolRuntimeInfo

Current runtime resource usage and state of the resource pool 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | [**ResourcePoolResourceUsage**](ResourcePoolResourceUsage.md) |  | 
**cpu** | [**ResourcePoolResourceUsage**](ResourcePoolResourceUsage.md) |  | 
**overall_status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**shares_scalable** | **str** | The scaling behavior of the shares of a given resource pool.  See *ResourceConfigSpecScaleSharesBehavior_enum* for possible values. The system will automatically compute this property based on the *ResourceConfigSpec.scaleDescendantsShares* setting on every ancestor resource pool. This property does not apply to virtual machines.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.resource_pool_runtime_info import ResourcePoolRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolRuntimeInfo from a JSON string
resource_pool_runtime_info_instance = ResourcePoolRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ResourcePoolRuntimeInfo.to_json()

# convert the object into a dict
resource_pool_runtime_info_dict = resource_pool_runtime_info_instance.to_dict()
# create an instance of ResourcePoolRuntimeInfo from a dict
resource_pool_runtime_info_form_dict = resource_pool_runtime_info.from_dict(resource_pool_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


