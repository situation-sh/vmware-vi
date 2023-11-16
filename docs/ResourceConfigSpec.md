# ResourceConfigSpec

This data object type is a specification for a set of resources allocated to a virtual machine or a resource pool. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**change_version** | **str** | The changeVersion is a unique identifier for a given version of the configuration.  Each change to the configuration will update this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.  If specified when updating the resource config., the changes will only be applied if the current changeVersion matches the specified changeVersion. This field can be used to guard against updates that has happened between the configInfo was read and until it is applied.  | [optional] 
**last_modified** | **datetime** | Timestamp when the resources were last modified.  This is ignored when the object is used to update a configuration.  | [optional] 
**cpu_allocation** | [**ResourceAllocationInfo**](ResourceAllocationInfo.md) |  | 
**memory_allocation** | [**ResourceAllocationInfo**](ResourceAllocationInfo.md) |  | 
**scale_descendants_shares** | **str** | Specifies the scaling behavior of the shares of all descendant resource pools under a given resource pool.  See *ResourceConfigSpecScaleSharesBehavior_enum* for possible values. If any scaling behavior other than *disabled* is specified, the system will scale the CPU and memory shares allocated to each descendant resource pool with the total shares of all powered on virtual machines under each respective pool. The system will also use the *SharesInfo* set on each descendant resource pool as a multiplier for the scale. If a resource pool&#39;s shares are already scalable through the *ResourceConfigSpec.scaleDescendantsShares* setting on an ancestor resource pool, the system will not allow *ResourceConfigSpec.scaleDescendantsShares* to be set on the resource pool. The *ResourcePoolRuntimeInfo.sharesScalable* property indicates whether or not a resource pool&#39;s shares are scalable. This property does not apply to virtual machines.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.resource_config_spec import ResourceConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceConfigSpec from a JSON string
resource_config_spec_instance = ResourceConfigSpec.from_json(json)
# print the JSON string representation of the object
print ResourceConfigSpec.to_json()

# convert the object into a dict
resource_config_spec_dict = resource_config_spec_instance.to_dict()
# create an instance of ResourceConfigSpec from a dict
resource_config_spec_form_dict = resource_config_spec.from_dict(resource_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


