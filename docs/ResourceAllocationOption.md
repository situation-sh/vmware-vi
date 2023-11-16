# ResourceAllocationOption

The ResourceAllocationOption data object specifies value ranges and default values for *ResourceAllocationInfo*.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares_option** | [**SharesOption**](SharesOption.md) |  | 

## Example

```python
from vmware_vi.models.resource_allocation_option import ResourceAllocationOption

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAllocationOption from a JSON string
resource_allocation_option_instance = ResourceAllocationOption.from_json(json)
# print the JSON string representation of the object
print ResourceAllocationOption.to_json()

# convert the object into a dict
resource_allocation_option_dict = resource_allocation_option_instance.to_dict()
# create an instance of ResourceAllocationOption from a dict
resource_allocation_option_form_dict = resource_allocation_option.from_dict(resource_allocation_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


