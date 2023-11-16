# DatacenterMismatch

The input arguments had entities that did not belong to the same datacenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_argument** | [**List[DatacenterMismatchArgument]**](DatacenterMismatchArgument.md) | The list of invalid arguments.  | 
**expected_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.datacenter_mismatch import DatacenterMismatch

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterMismatch from a JSON string
datacenter_mismatch_instance = DatacenterMismatch.from_json(json)
# print the JSON string representation of the object
print DatacenterMismatch.to_json()

# convert the object into a dict
datacenter_mismatch_dict = datacenter_mismatch_instance.to_dict()
# create an instance of DatacenterMismatch from a dict
datacenter_mismatch_form_dict = datacenter_mismatch.from_dict(datacenter_mismatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


