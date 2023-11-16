# DatacenterMismatchArgument

An input entity argument that belongs to a mismatched datacenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**input_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.datacenter_mismatch_argument import DatacenterMismatchArgument

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterMismatchArgument from a JSON string
datacenter_mismatch_argument_instance = DatacenterMismatchArgument.from_json(json)
# print the JSON string representation of the object
print DatacenterMismatchArgument.to_json()

# convert the object into a dict
datacenter_mismatch_argument_dict = datacenter_mismatch_argument_instance.to_dict()
# create an instance of DatacenterMismatchArgument from a dict
datacenter_mismatch_argument_form_dict = datacenter_mismatch_argument.from_dict(datacenter_mismatch_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


