# SwapPlacementOverrideNotSupported

The virtual machine is configured to override the default swapfile placement policy, which is not supported on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.swap_placement_override_not_supported import SwapPlacementOverrideNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of SwapPlacementOverrideNotSupported from a JSON string
swap_placement_override_not_supported_instance = SwapPlacementOverrideNotSupported.from_json(json)
# print the JSON string representation of the object
print SwapPlacementOverrideNotSupported.to_json()

# convert the object into a dict
swap_placement_override_not_supported_dict = swap_placement_override_not_supported_instance.to_dict()
# create an instance of SwapPlacementOverrideNotSupported from a dict
swap_placement_override_not_supported_form_dict = swap_placement_override_not_supported.from_dict(swap_placement_override_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


