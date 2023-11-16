# ArrayOfOpaqueNetworkSummary

A boxed array of *OpaqueNetworkSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OpaqueNetworkSummary]**](OpaqueNetworkSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_opaque_network_summary import ArrayOfOpaqueNetworkSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOpaqueNetworkSummary from a JSON string
array_of_opaque_network_summary_instance = ArrayOfOpaqueNetworkSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfOpaqueNetworkSummary.to_json()

# convert the object into a dict
array_of_opaque_network_summary_dict = array_of_opaque_network_summary_instance.to_dict()
# create an instance of ArrayOfOpaqueNetworkSummary from a dict
array_of_opaque_network_summary_form_dict = array_of_opaque_network_summary.from_dict(array_of_opaque_network_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


